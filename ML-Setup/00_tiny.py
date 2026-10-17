# import torch

# x = torch.tensor([1.0, 2.0, 3.0])   # 造一个数组
# print(x)
# print(x.shape)                       # 它的形状

# y = x * 2 + 1                        # 对整个数组做运算，不用写 for
# print(y)
# print(y.shape)    

# img = torch.zeros(1, 28, 28)         # 造一张全黑的"图"：1 个通道，28 行，28 列
# print(img.shape)

# batch=torch.zeros(4,1,28,28)
# print(batch.shape)

# flat=batch.flatten(1)
# print(flat.shape)

import torch
import torch.nn as nn
import torch.nn.functional as F

model = nn.Sequential(
    nn.Conv2d(1, 16, 3, padding=1),
    nn.ReLU(),
    nn.MaxPool2d(2),
    nn.Conv2d(16, 32, 3, padding=1),
    nn.ReLU(),
    nn.MaxPool2d(2),
    nn.Flatten(),
    nn.Linear(32 * 7 * 7, 10),
)

x = torch.zeros(1, 1, 28, 28)   # 一张 28×28 的灰度图
y = model(x)
print(y.shape)                  # 猜猜是多少
print(y)  