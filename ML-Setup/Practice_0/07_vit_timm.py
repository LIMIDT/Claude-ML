"""
第 7 周：timm 的 ViT-Tiny 在 CIFAR-10 上，对比"预训练"和"从零训练"

只改一个变量：PRETRAINED。其余设置两次完全相同。
用法：先 PRETRAINED = True 跑一次，再改成 False 跑一次，记下两次的结果。
"""
import time
import torch
import torch.nn as nn
import torch.nn.functional as F
import timm
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

PRETRAINED = False      # <-- 唯一要改的地方：第一次 True，第二次 False
EPOCHS = 5             
LR = 1e-4
BATCH_SIZE=64

torch.manual_seed(0)
device = "cuda" if torch.cuda.is_available() else "cpu"
print("使用设备:", device, "| PRETRAINED =", PRETRAINED)

# 1. 数据
# CIFAR-10 原图是 32x32，ViT 要 224x224。放大这一步放到 GPU 上做，比在 CPU 上快
train_tf = transforms.Compose([
    transforms.RandomCrop(32, padding=4),
    transforms.RandomHorizontalFlip(),
    transforms.ToTensor(),
])
test_tf = transforms.ToTensor()

train_set = datasets.CIFAR10("./data", train=True, download=True, transform=train_tf)
test_set = datasets.CIFAR10("./data", train=False, download=True, transform=test_tf)
train_loader = DataLoader(train_set, batch_size=BATCH_SIZE, shuffle=True, num_workers=0)
test_loader = DataLoader(test_set, batch_size=256, shuffle=False, num_workers=0)


def prepare(images):
    images = images.to(device)
    images = F.interpolate(images, size=224, mode="bilinear", align_corners=False)  # 32 -> 224
    return (images - 0.5) / 0.5    # 这个预训练模型要求的归一化：均值 0.5、标准差 0.5


# 2. 模型：同一个结构，只有"权重是不是预训练的"不同
#    num_classes=10：最后的分类头换成 10 类（预训练原本是 1000 类），这一层总是随机初始化
model = timm.create_model("vit_tiny_patch16_224", pretrained=PRETRAINED, num_classes=10).to(device)
print("参数量:", f"{sum(p.numel() for p in model.parameters()):,}")

# 3. 优化器 + 学习率调度（两次完全一样）
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.AdamW(model.parameters(), lr=LR, weight_decay=0.05)
scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=EPOCHS)

# 4. 训练 + 测试
best_acc = 0.0
for epoch in range(1, EPOCHS + 1):
    t0 = time.time()
    model.train()
    total_loss = 0.0
    for images, labels in train_loader:
        images, labels = prepare(images), labels.to(device)
        loss = criterion(model(images), labels)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    scheduler.step()

    model.eval()
    correct = 0
    with torch.no_grad():
        for images, labels in test_loader:
            images, labels = prepare(images), labels.to(device)
            correct += (model(images).argmax(1) == labels).sum().item()
    acc = correct / len(test_set)
    best_acc = max(best_acc, acc)

    print(f"epoch {epoch}/{EPOCHS}: 平均 loss = {total_loss / len(train_loader):.4f}, "
          f"测试准确率 = {acc:.2%}, 用时 {time.time() - t0:.0f}s")

print(f"\nPRETRAINED = {PRETRAINED}，最好测试准确率 = {best_acc:.2%}")
