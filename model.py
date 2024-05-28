import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F

class PaddleNet(nn.Module):
    def __init__(self):
        super(PaddleNet, self).__init__()
        self.fc1 = nn.Linear(5, 24)
        self.fc2 = nn.Linear(24, 24)
        self.fc3 = nn.Linear(24, 1)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = torch.tanh(self.fc3(x))
        return x
