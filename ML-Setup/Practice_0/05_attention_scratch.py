import math
from turtle import forward
import torch
import torch.nn as nn

class MySelfAttention(nn.Module):
    def __init__(self, d_model):
        super().__init__()
        self.wq = nn.Linear(d_model, d_model, bias=False)
        self.wk = nn.Linear(d_model, d_model, bias=False)
        self.wv = nn.Linear(d_model, d_model, bias=False)

    def forward(self, x):
        q, k, v = self.wq(x), self.wk(x), self.wv(x)
        scores = scores = q @ k.transpose(-2, -1) / math.sqrt(q.size(-1))
        weights = torch.softmax(scores, dim=-1)
        return weights @ v 

torch.manual_seed(0)
B, n, d = 2, 5, 8
x = torch.randn(B, n, d)
mine = MySelfAttention(d)

ref = nn.MultiheadAttention(d, num_heads=1, bias=False, batch_first=True)
with torch.no_grad():
    ref.in_proj_weight.copy_(torch.cat([mine.wq.weight, mine.wk.weight, mine.wv.weight], dim=0))
    ref.out_proj.weight.copy_(torch.eye(d))

out_mine = mine(x)
out_ref, _ = ref(x, x, x)
print("形状:", out_mine.shape, out_ref.shape)
print("allclose:", torch.allclose(out_mine, out_ref, atol=1e-5))
print("最大差值:", (out_mine - out_ref).abs().max().item())
