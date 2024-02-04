import torch
import torch.nn as nn


class NN(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(NN, self).__init__()
        self.l1 = nn.Linear(input_size, hidden_size) 
        self.l2 = nn.Linear(hidden_size, hidden_size) 
        self.l3 = nn.Linear(hidden_size, num_classes)
        self.relu = nn.ReLU()
    
    def forward(self, x):
        x1 = self.l1(x)
        x1 = self.relu(x1)
        x2 = self.l2(x1)
        x2 = self.relu(x2)
        out = self.l3(x2)
        return out