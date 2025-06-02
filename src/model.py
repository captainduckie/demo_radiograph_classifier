import torch.nn as nn
import torchvision.models as models

class MultiLabelCNN(nn.Module):
    def __init__(self, num_labels):
        super().__init__()
        self.base = models.resnet50(pretrained=True)
        self.base.fc = nn.Linear(self.base.fc.in_features, num_labels)

    def forward(self, x):
        return self.base(x)
