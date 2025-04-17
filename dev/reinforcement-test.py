import gym
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import random
from collections import deque

# Hyperparameters
GAMMA = 0.99
LR = 1e-3
BATCH_SIZE = 64
MEMORY_SIZE = 10000
EPSILON_START = 1.0
EPSILON_END = 0.01
EPSILON_DECAY = 0.995
TARGET_UPDATE = 10
NUM_EPISODES = 500

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Neural Network for Q-learning
class QNetwork(nn.Module):
    def __init__(self, obs_dim, action_dim):
        super(QNetwork, self).__init__()
        self.fc = nn.Sequential(
            nn.Linear(obs_dim, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, action_dim)
        )

    def forward(self, x):
        return self.fc(x)

# Replay Memory
class ReplayBuffer:
    def __init__(self, capacity):
        self.buffer = deque(maxlen=capacity)

    def push(self, state, action, reward, next_state, done):
        self.buffer.append((state, action, reward, next_state, done))

    def sample(self, batch_size):
        samples = random.sample(self.buffer, batch_size)
        states, actions, rewards, next_states, dones = zip(*samples)
        return (torch.tensor(states, dtype=torch.float32).to(device),
                torch.tensor(actions).to(device),
                torch.tensor(rewards, dtype=torch.float32).to(device),
                torch.tensor(next_states, dtype=torch.float32).to(device),
                torch.tensor(dones, dtype=torch.float32).to(device))

    def __len__(self):
        return len(self.buffer)

# Epsilon-greedy action selection
def select_action(state, epsilon, q_net, action_dim):
    if random.random() < epsilon:
        return random.randrange(action_dim)
    else:
        with torch.no_grad():
            state = torch.tensor(state, dtype=torch.float32).unsqueeze(0).to(device)
            q_values = q_net(state)
            return q_values.argmax().item()

# Training loop
def train():
    env = gym.make("CartPole-v1")
    obs_dim = env.observation_space.shape[0]
    action_dim = env.action_space.n

    q_net = QNetwork(obs_dim, action_dim).to(device)
    target_net = QNetwork(obs_dim, action_dim).to(device)
    target_net.load_state_dict(q_net.state_dict())

    optimizer = optim.Adam(q_net.parameters(), lr=LR)
    memory = ReplayBuffer(MEMORY_SIZE)

    epsilon = EPSILON_START

    for episode in range(NUM_EPISODES):
        state = env.reset()[0]  # [0] for Gym >= 0.26
        total_reward = 0

        for t in range(1, 1000):  # Cap max steps
            action = select_action(state, epsilon, q_net, action_dim)
            next_state, reward, done, _, _ = env.step(action)
            memory.push(state, action, reward, next_state, done)

            state = next_state
            total_reward += reward

            if len(memory) >= BATCH_SIZE:
                states, actions, rewards, next_states, dones = memory.sample(BATCH_SIZE)

                # Q(s, a)
                q_values = q_net(states).gather(1, actions.unsqueeze(1)).squeeze()

                # max_a' Q_target(s', a')
                next_q_values = target_net(next_states).max(1)[0]
                target = rewards + GAMMA * next_q_values * (1 - dones)

                loss = nn.MSELoss()(q_values, target)

                optimizer.zero_grad()
                loss.backward()
                optimizer.step()

            if done:
                break

        epsilon = max(EPSILON_END, epsilon * EPSILON_DECAY)

        if episode % TARGET_UPDATE == 0:
            target_net.load_state_dict(q_net.state_dict())

        print(f"Episode {episode}, Reward: {total_reward}, Epsilon: {epsilon:.3f}")

    env.close()

if __name__ == "__main__":
    train()
