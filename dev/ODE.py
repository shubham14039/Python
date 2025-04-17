import torch
import torch.nn as nn
import matplotlib.pyplot as plt
from torchdiffeq import odeint

# Define the ODE Function
class ODEFunc(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(2, 50),
            nn.Tanh(),
            nn.Linear(50, 2)
        )

    def forward(self, t, x):
        return self.net(x)

# Define the Neural ODE model
class NeuralODE(nn.Module):
    def __init__(self, ode_func):
        super().__init__()
        self.ode_func = ode_func

    def forward(self, x0, t):
        return odeint(self.ode_func, x0, t)

# Create synthetic spiral data
def get_spiral():
    t = torch.linspace(0, 2 * 3.14, 100)
    x = torch.stack([torch.sin(t), torch.cos(t)], dim=1) * torch.exp(-0.1 * t).unsqueeze(1)
    return x, t

# Training loop
def train():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    x_true, t = get_spiral()
    x_true, t = x_true.to(device), t.to(device)

    ode_func = ODEFunc().to(device)
    model = NeuralODE(ode_func).to(device)

    optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
    loss_fn = nn.MSELoss()

    for itr in range(1000):
        optimizer.zero_grad()
        x0 = x_true[0]
        pred_x = model(x0, t)
        loss = loss_fn(pred_x, x_true)
        loss.backward()
        optimizer.step()

        if itr % 100 == 0:
            print(f"Iter {itr}, Loss: {loss.item():.6f}")

    return model, x_true, t

# Plotting
def plot(model, x_true, t):
    x0 = x_true[0]
    pred_x = model(x0, t).detach().cpu()
    x_true = x_true.cpu()

    plt.figure(figsize=(6, 6))
    plt.plot(x_true[:, 0], x_true[:, 1], label="True", linewidth=2)
    plt.plot(pred_x[:, 0], pred_x[:, 1], label="Predicted", linestyle='--')
    plt.legend()
    plt.title("Neural ODE Fit to Spiral Trajectory")
    plt.xlabel("x1"); plt.ylabel("x2")
    plt.axis('equal')
    plt.grid()
    plt.show()

if __name__ == "__main__":
    model, x_true, t = train()
    plot(model, x_true, t)
