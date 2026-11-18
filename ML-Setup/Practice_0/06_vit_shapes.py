"""
第 7 周：看清楚一张图片在 ViT 里每一步变成什么形状
对照论文公式 (1)，一步一步打印，不训练。
"""
import torch
from einops import repeat
from vit_lucid import ViT

torch.manual_seed(0)

model = ViT(
    image_size=224,   # 图片 224x224
    patch_size=16,    # 每块 16x16
    num_classes=10,
    dim=512,          # 每个块变成 512 维向量（ViT-Base 的设置）
    depth=2,          # 只叠 2 层，够看形状就行
    heads=12,
    mlp_dim=3072,
)

img = torch.randn(2, 3, 224, 224)               # 2 张假图片
print("1 输入图片:", img.shape)

x = model.to_patch_embedding[0](img)             # 只做切块+展平
print("2 切块展平后:", x.shape)

x = model.to_patch_embedding(img)                # 切块 + 线性映射成 768 维
print("3 映射成向量后:", x.shape)

cls = repeat(model.cls_token, "... d -> b ... d", b=img.shape[0])
x = torch.cat((cls, x), dim=1)                   # 最前面拼上分类 token
print("4 拼上 cls token:", x.shape)

x = x + model.pos_embedding[: x.shape[1]]        # 加位置编码，形状不变
print("5 加位置编码后:", x.shape)

x = model.transformer(x)                          # 过 Transformer，形状不变
print("6 Transformer 输出:", x.shape)

out = model.mlp_head(x[:, 0])                     # 只取第 0 个位置做分类
print("7 分类结果:", out.shape)

print("\n参数量:", sum(p.numel() for p in model.parameters()))
