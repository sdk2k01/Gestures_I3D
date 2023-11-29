import cv2
import torch
import torch.nn as nn
import torch.nn.functional as F

class GestNet(nn.Module):
    def __init__(self, in_ch: int):
        super(GestNet, self).__init__()
        self.first_layer = nn.Sequential(
            nn.Conv3d(in_ch, 32, (1, 3, 3), (1, 3, 3)),
            nn.BatchNorm3d(32),
            nn.ReLU()
        )
        
        self.stack_2_1 = nn.Sequential(
            nn.Conv3d(32, 32, (1, 1, 1), stride=(1, 2, 2)),
            nn.BatchNorm3d(32),
            nn.ReLU(),
            nn.Conv3d(32, 32, (1, 3, 3), padding='same'),
            nn.BatchNorm3d(32),
            nn.ReLU(),
            nn.Conv3d(32, 128, (1, 1, 1)),
            nn.BatchNorm3d(128),
        )
        
        self.res_2_1 = nn.Sequential(
            nn.Conv3d(32, 128, (1, 1, 1), stride=(1, 2, 2)),
            nn.BatchNorm3d(128)                        
        )
        
        self.stack_2_2 = nn.Sequential(
            nn.Conv3d(128, 32, (1, 1, 1)),
            nn.BatchNorm3d(32),
            nn.ReLU(),
            nn.Conv3d(32, 32, (1, 3, 3), padding='same'),
            nn.BatchNorm3d(32),
            nn.ReLU(),
            nn.Conv3d(32, 128, (1, 1, 1)),
            nn.BatchNorm3d(128),
        )
        
        self.stack_2_3 = nn.Sequential(
            nn.Conv3d(128, 32, (1, 1, 1)),
            nn.BatchNorm3d(32),
            nn.ReLU(),
            nn.Conv3d(32, 32, (1, 3, 3), padding='same'),
            nn.BatchNorm3d(32),
            nn.ReLU(),
            nn.Conv3d(32, 128, (1, 1, 1)),
            nn.BatchNorm3d(128),
        )
        
        self.stack_2_4 = nn.Sequential(
            nn.Conv3d(128, 32, (1, 1, 1)),
            nn.BatchNorm3d(32),
            nn.ReLU(),
            nn.Conv3d(32, 32, (1, 3, 3), padding='same'),
            nn.BatchNorm3d(32),
            nn.ReLU(),
            nn.Conv3d(32, 128, (1, 1, 1)),
            nn.BatchNorm3d(128)
        )
        
        self.stack_3_1 = nn.Sequential(
            nn.Conv3d(128, 64, (3, 1, 1), padding=(1, 0, 0), stride=(1, 2, 2)),
            nn.BatchNorm3d(64),
            nn.ReLU(),
            nn.Conv3d(64, 64, (1, 3, 3), padding='same'),
            nn.BatchNorm3d(64),
            nn.ReLU(),
            nn.Conv3d(64, 256, (1, 1, 1)),
            nn.BatchNorm3d(256),
        )
        
        self.res_3_1 = nn.Sequential(
            nn.Conv3d(128, 256, (1, 1, 1), stride=(1, 2, 2)),
            nn.BatchNorm3d(256)                        
        )
        
        self.stack_3_2 = nn.Sequential(
            nn.Conv3d(256, 64, (3, 1, 1), padding='same'),
            nn.BatchNorm3d(64),
            nn.ReLU(),
            nn.Conv3d(64, 64, (1, 3, 3), padding='same'),
            nn.BatchNorm3d(64),
            nn.ReLU(),
            nn.Conv3d(64, 256, (1, 1, 1)),
            nn.BatchNorm3d(256),
        )
        
        self.stack_3_3 = nn.Sequential(
            nn.Conv3d(256, 64, (3, 1, 1), padding='same'),
            nn.BatchNorm3d(64),
            nn.ReLU(),
            nn.Conv3d(64, 64, (1, 3, 3), padding='same'),
            nn.BatchNorm3d(64),
            nn.ReLU(),
            nn.Conv3d(64, 256, (1, 1, 1)),
            nn.BatchNorm3d(256),
        )
        
        self.stack_3_4 = nn.Sequential(
            nn.Conv3d(256, 64, (3, 1, 1), padding='same'),
            nn.BatchNorm3d(64),
            nn.ReLU(),
            nn.Conv3d(64, 64, (1, 3, 3), padding='same'),
            nn.BatchNorm3d(64),
            nn.ReLU(),
            nn.Conv3d(64, 256, (1, 1, 1)),
            nn.BatchNorm3d(256),
        )
        
        self.stack_3_5 = nn.Sequential(
            nn.Conv3d(256, 64, (3, 1, 1), padding='same'),
            nn.BatchNorm3d(64),
            nn.ReLU(),
            nn.Conv3d(64, 64, (1, 3, 3), padding='same'),
            nn.BatchNorm3d(64),
            nn.ReLU(),
            nn.Conv3d(64, 256, (1, 1, 1)),
            nn.BatchNorm3d(256),
        )
        
        self.stack_3_6 = nn.Sequential(
            nn.Conv3d(256, 64, (3, 1, 1), padding='same'),
            nn.BatchNorm3d(64),
            nn.ReLU(),
            nn.Conv3d(64, 64, (1, 3, 3), padding='same'),
            nn.BatchNorm3d(64),
            nn.ReLU(),
            nn.Conv3d(64, 256, (1, 1, 1)),
            nn.BatchNorm3d(256),
        )
        
        self.stack_4_1 = nn.Sequential(
            nn.Conv3d(256, 128, (3, 1, 1), padding=(1, 0, 0), stride=(1, 2, 2)),
            nn.BatchNorm3d(128),
            nn.ReLU(),
            nn.Conv3d(128, 128, (1, 3, 3), padding='same'),
            nn.BatchNorm3d(128),
            nn.ReLU(),
            nn.Conv3d(128, 512, (1, 1, 1)),
            nn.BatchNorm3d(512),
        )
        
        self.res_4_1 = nn.Sequential(
            nn.Conv3d(256, 512, (1, 1, 1), stride=(1, 2, 2)),
            nn.BatchNorm3d(512)                        
        )
        
        self.stack_4_2 = nn.Sequential(
            nn.Conv3d(512, 128, (3, 1, 1), padding='same'),
            nn.BatchNorm3d(128),
            nn.ReLU(),
            nn.Conv3d(128, 128, (1, 3, 3), padding='same'),
            nn.BatchNorm3d(128),
            nn.ReLU(),
            nn.Conv3d(128, 512, (1, 1, 1)),
            nn.BatchNorm3d(512),
        )
        
        self.stack_4_3 = nn.Sequential(
            nn.Conv3d(512, 128, (3, 1, 1), padding='same'),
            nn.BatchNorm3d(128),
            nn.ReLU(),
            nn.Conv3d(128, 128, (1, 3, 3), padding='same'),
            nn.BatchNorm3d(128),
            nn.ReLU(),
            nn.Conv3d(128, 512, (1, 1, 1)),
            nn.BatchNorm3d(512),
        )
        
        
    def forward(self, x):
        first_layer_out = self.first_layer(x)
        residual = first_layer_out

        second_stack_1 = self.stack_2_1(first_layer_out)
        residual = self.res_2_1(residual)
        second_stack_1 += residual
        second_stack_1 = F.relu(second_stack_1)
        residual = second_stack_1
        
        second_stack_2 = self.stack_2_2(second_stack_1)
        second_stack_2 += residual
        second_stack_2 = F.relu(second_stack_2)
        residual = second_stack_2
        
        second_stack_3 = self.stack_2_3(second_stack_2)
        second_stack_3 += residual
        second_stack_3 = F.relu(second_stack_3)
        residual = second_stack_3
        
        second_stack_4 = self.stack_2_4(second_stack_3)
        second_stack_4 += residual
        second_stack_4 = F.relu(second_stack_4)
        residual = second_stack_4
        
        third_stack_1 = self.stack_3_1(second_stack_4)
        residual = self.res_3_1(residual)
        third_stack_1 += residual
        third_stack_1 = F.relu(third_stack_1)
        residual = third_stack_1
        
        third_stack_2 = self.stack_3_2(third_stack_1)
        third_stack_2 += residual
        third_stack_2 = F.relu(third_stack_1)
        residual = third_stack_2
        
        third_stack_3 = self.stack_3_3(third_stack_2)
        third_stack_3 += residual
        third_stack_3 = F.relu(third_stack_2)
        residual = third_stack_3
        
        third_stack_4 = self.stack_3_4(third_stack_3)
        third_stack_4 += residual
        third_stack_4 = F.relu(third_stack_3)
        residual = third_stack_4
        
        third_stack_5 = self.stack_3_5(third_stack_4)
        third_stack_5 += residual
        third_stack_5 = F.relu(third_stack_4)
        residual = third_stack_5
        
        third_stack_6 = self.stack_3_6(third_stack_5)
        third_stack_6 += residual
        third_stack_6 = F.relu(third_stack_6)
        residual = third_stack_6
        
        fourth_stack_1 = self.stack_4_1(third_stack_6)
        residual = self.res_4_1(residual)
        fourth_stack_1 += residual
        fourth_stack_1 = F.relu(fourth_stack_1)
        residual = fourth_stack_1
        
        fourth_stack_2 = self.stack_4_2(fourth_stack_1)
        fourth_stack_2 += residual
        fourth_stack_2 = F.relu(fourth_stack_2)
        residual = fourth_stack_2
        
        fourth_stack_3 = self.stack_4_3(fourth_stack_2)
        fourth_stack_3 += residual
        fourth_stack_3 = F.relu(fourth_stack_3)
        residual = fourth_stack_3
        
        return residual

def preprocess(frame_list):
    # Convert frames to PyTorch tensors
    tensor_list = [torch.tensor(frame.transpose((2, 0, 1)), dtype=torch.float32) for frame in frame_list]

    # Stack tensors along the first dimension to create a batch
    tensor_batch = torch.stack(tensor_list, dim=1)

    # Add a batch dimension (1) at the beginning
    tensor_batch = tensor_batch.unsqueeze(0)

    # # Print the shape of the resulting tensor
    # print(tensor_batch.shape)

    return tensor_batch

def predict(tensor_input):
    model = GestNet(3)
    model.eval()
    # rand = torch.rand((1, 3, 4, 224, 224))
    out = model(tensor_input)
    print(out.size())

# predict()