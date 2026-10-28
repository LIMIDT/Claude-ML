"""
第四个深度学习程序：用 ResNet18 在 CIFAR-10 上冲到 90%+

和 02_cifar10.py 的区别：
  1. 模型换成了现成的 ResNet18（torchvision 里就有），不再是两层小卷积
  2. 加了数据增强（随机裁剪 + 随机翻转），让模型见到更多样的图
  3. 学习率随训练进程衰减（CosineAnnealingLR），后期步子变小，冲更高准确率

阶段 0 的目标是 85%，这个脚本正常跑完应该在 90% 以上。
"""
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms, models

torch.manual_seed(0)                 # 固定随机种子，结果可复现
device = "cuda" if torch.cuda.is_available() else "cpu"
print("使用设备:", device)

# 1. 数据
# 训练集加数据增强：每轮看到的图都不完全一样，模型不容易死记硬背
train_transform = transforms.Compose([
    transforms.RandomCrop(32, padding=4),        # 先四周补 4 像素，再随机裁回 32x32
    transforms.RandomHorizontalFlip(),           # 一半概率左右翻转
    transforms.ToTensor(),
    transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2470, 0.2435, 0.2616)),
])

# 测试集不能增强，只做和训练一致的标准化
test_transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2470, 0.2435, 0.2616)),
])

train_set = datasets.CIFAR10("./data", train=True, download=True, transform=train_transform)
test_set = datasets.CIFAR10("./data", train=False, download=True, transform=test_transform)

train_loader = DataLoader(train_set, batch_size=128, shuffle=True, num_workers=0)
test_loader = DataLoader(test_set, batch_size=256, shuffle=False, num_workers=0)

print(f"训练集 {len(train_set)} 张，测试集 {len(test_set)} 张，训练集共 {len(train_loader)} 个 batch")

# 2. 模型：直接调用 torchvision 里写好的 ResNet18
#    原本它是给 1000 类 ImageNet 用的，这里把最后一层的输出改成 10 类
model = models.resnet18(num_classes=10).to(device)

n_params = sum(p.numel() for p in model.parameters())
print(f"模型参数量: {n_params:,}")

# 3. 优化器 + 学习率调度
n_epochs = 30
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

# 余弦退火：学习率从 1e-3 开始，一路沿着余弦曲线降到接近 0
# 前期步子大、学得快；后期步子小，能在最优点附近停稳
scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=n_epochs)

criterion = nn.CrossEntropyLoss()
best_acc = 0.0

# 4. 训练 + 测试
for epoch in range(1, n_epochs + 1):
    model.train()
    total_loss = 0.0
    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)
        loss = criterion(model(images), labels)

        optimizer.zero_grad()      # 清空上一步的梯度
        loss.backward()            # 反向传播，算出每个参数的梯度
        optimizer.step()           # 按梯度更新参数

        total_loss += loss.item()

    scheduler.step()               # 每轮结束后调整一次学习率

    # 测试集上算准确率
    model.eval()
    correct = 0
    with torch.no_grad():
        for images, labels in test_loader:
            images, labels = images.to(device), labels.to(device)
            correct += (model(images).argmax(1) == labels).sum().item()

    acc = correct / len(test_set)
    lr_now = optimizer.param_groups[0]["lr"]
    print(
        f"epoch {epoch:2d}/{n_epochs}: "
        f"平均 loss = {total_loss / len(train_loader):.4f}, "
        f"测试准确率 = {acc:.2%}, "
        f"当前学习率 = {lr_now:.2e}"
    )

    if acc > best_acc:
        best_acc = acc
        torch.save(model.state_dict(), "cifar10_resnet18.pt")
        print(f"   -> 新的最好成绩 {best_acc:.2%}，已保存")

print(f"\n训练结束，最好测试准确率 = {best_acc:.2%}")
