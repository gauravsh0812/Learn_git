import torch
import torch.nn as nn
import torch.nn.functional as F

is_cuda = torch.cuda.is_available()
if is_cuda: device = torch.device('cuda')
else: device = torch.device('cpu')

class CNN(nn.Module):
    def __init__(self):
        # Initializing the inherited and parent class
        super(CNN, self).__init__()

        # defining conv2d layers with kernel size of 3x3
        self.conv1 = nn.conv2d(1, 64, 3)
        self.bn1 = nn.BatchNorm2d(num_features=64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.conv2 = nn.conv2d(64, 128, 3)
        self.bn2 = nn.BatchNorm2d(num_features=128, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.conv3 = nn.conv2d(128, 256, 3)
        self.bn3 = nn.BatchNorm2d(num_features=256, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.conv4 = nn.conv2d(256, 512, 3)
        self.bn4 = nn.BatchNorm2d(num_features=512, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.conv5 = nn.conv2d(512, 512, 3)
        self.bn5 = nn.BatchNorm2d(num_features=512, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)

        # flattening
        self.fc1 = nn.Linear(self._to_linear, 512)

        def convs(self, x):
            x = F.max_pool2d(F.relu(self.bn1(self.conv1(x))), (2, 2))
            x = F.max_pool2d(F.relu(self.bn2(self.conv2(x))), (2, 2))
            x = F.max_pool2d(F.relu(self.bn3(self.conv3(x))), (2, 2))
            x = F.max_pool2d(F.relu(self.bn4(self.conv4(x))), (2, 2))
            x = F.max_pool2d(F.relu(self.bn5(self.conv5(x))), (2, 2))

            # shape of the image
            self._to_linear = x[0].shape[0]*x[0].shape[1]*x[0].shape[2]

            return x

        def forward(self, x):
            x = self.convs(x)
            x = x.view(-1, self._to_linear)  # .view is reshape ... this flattens X before
            x = F.relu(self.fc1(x))

# This layer meant to be fed in LSTM
class LSTM(nn.Module):
    def __init__(self):
        super(CNN2LSTM, self).__init__()
        self.cnn = CNN()
        CNN c1 =
        self.output_size = #self._to_linear
        self.num_hidden = num_hidden
        self.num_layers = num_layers
        self.dropout = dropout
        self.vocab_size = vocab_size
        self.embedding_dim = embedding_dim

        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.lstm = nn.LSTM(embedding_dim, hidden_dim, n_layers, dropout=dropout, batch_first=True)
        self.dropout = nn.Dropout(dropout)
        self.lstm_fc1 = nn.Linear(embedding_dim, output_size)
