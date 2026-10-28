# 自检脚本：装完环境后运行，确认 PyTorch 能用
import sys
import torch

print("Python  :", sys.version.split()[0])
print("PyTorch :", torch.__version__)
print("CUDA 可用:", torch.cuda.is_available())
if torch.cuda.is_available():
    print("显卡    :", torch.cuda.get_device_name(0))

# 做一次真正的计算，确认不是只装了个壳
x = torch.randn(256, 256)
y = x @ x.T
assert y.shape == (256, 256)
if torch.cuda.is_available():
    yg = (x.cuda() @ x.cuda().T).cpu()
    assert torch.allclose(y, yg, atol=1e-3)
print("矩阵乘法测试通过，环境 OK。")
