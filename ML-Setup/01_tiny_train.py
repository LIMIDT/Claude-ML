import torch
import torch.nn as nn

# 造一点假数据：10 张"图"，每张是 1x4x4（不用真的 MNIST，先看懂训练本身）
x = torch.randn(10, 1, 4, 4)          # 10 张假图
y = torch.randint(0, 2, (10,))         # 10 个正确答案，只有 0 或 1 两类

model = nn.Sequential(
    nn.Flatten(),
    nn.Linear(1 * 4 * 4, 2),            # 16个数 -> 2个类别的分数
)

optimizer = torch.optim.SGD(model.parameters(), lr=0.1)

for step in range(20):
    pred = model(x)                               # 过一遍模型，得到预测分数
    loss = nn.functional.cross_entropy(pred, y)    # 算"错得有多离谱"
    optimizer.zero_grad()                          # 清零上一次的记录
    loss.backward()                                # 算出每个参数该往哪改
    optimizer.step()                               # 真的去改参数
    print(f"第{step}步, loss = {loss.item():.4f}")