"""
第二个深度学习程序：CIFAR-10 图片分类（10 类 32x32 彩色图）
目的：在 MNIST 基础上把数据集换成 CIFAR-10，看 loss 下降、准确率上升。
看懂每一行之后，可以试着加网络层或数据增强，冲更高的准确率。
"""
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

device = "cuda" if torch.cuda.is_available() else "cpu"
print("使用设备:", device)

# 1. 数据：第一次运行会自动下载到 ./data (约 163MB)
transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2470, 0.2435, 0.2616))])
train_set = datasets.CIFAR10("./data", train=True, download=True, transform=transform)
test_set = datasets.CIFAR10("./data", train=False, download=True, transform=transform)
train_loader = DataLoader(train_set, batch_size=128, shuffle=True)
test_loader = DataLoader(test_set, batch_size=1000)

img, label = train_set[0]
print(img.shape, label)        # 应该是 torch.Size([3, 32, 32]) 和一个数字
print(len(train_loader))       # 应该是 391 (50000 / 128 向上取整)

# 2. 模型：一个很小的卷积网络
class Net(nn.Module):                          # 定义一个新的"模型"，继承自 nn.Module
    def __init__(self):                        # 初始化：这里只"声明用了哪些零件"
        super().__init__()
        self.conv1 = nn.Conv2d(3, 16, 3, padding=1)   # 零件1：卷积，3通道进，16通道出  卷积，第一个通道进，第二个出，只改变通道数
        self.conv2 = nn.Conv2d(16, 32, 3, padding=1)  # 零件2：卷积，16通道进，32通道出
        self.fc = nn.Linear(32 * 8 * 8, 10)           # 零件3：全连接，2048个数进，10个分数出

    def forward(self, x):                      # 数据"流过去"的路线
        x = F.max_pool2d(F.relu(self.conv1(x)), 2)   # 过零件1，再压缩一半尺寸  池化，宽和高各自除以二
        x = F.max_pool2d(F.relu(self.conv2(x)), 2)   # 过零件2，再压缩一半尺寸
        return self.fc(x.flatten(1))                  # 拍平，过零件3，输出10个类别的分数


model = Net().to(device)
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

# 3. 训练 + 测试
for epoch in range(1, 4):
    model.train()
    total_loss = 0.0
    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)
        loss = F.cross_entropy(model(images), labels)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        total_loss += loss.item()

    model.eval()
    correct = 0
    with torch.no_grad():
        for images, labels in test_loader:
            images, labels = images.to(device), labels.to(device)
            correct += (model(images).argmax(1) == labels).sum().item()

    print(f"epoch {epoch}: 平均 loss = {total_loss / len(train_loader):.4f}, 测试准确率 = {correct / len(test_set):.2%}")

print("跑通了。")
