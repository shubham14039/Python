
import torch.nn as nn

model = nn.Sequential(
    nn.Linear(4, 3),    # f1
    nn.ReLU(),          # f2
    nn.Linear(3, 1)     # f3
)

# model(x) = f3(f2(f1(x)))
