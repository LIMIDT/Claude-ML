@echo off
title 修复: 换成 CUDA 版 PyTorch
set "PY=%USERPROFILE%\miniconda3\envs\ml\python.exe"
set "PIP_MIRROR=https://pypi.org/simple/"
set "TORCH_MIRROR=https://download.pytorch.org/whl/cu128"
echo ======== 显卡驱动信息 ========
nvidia-smi
echo.
echo ======== 卸载 CPU 版 ========
"%PY%" -m pip uninstall -y torch torchvision
echo.
echo ======== 安装 CUDA 12.8 版  约 2.5GB, 耐心等 ========
"%PY%" -m pip install --index-url %TORCH_MIRROR% --extra-index-url %PIP_MIRROR% torch==2.11.0+cu128 torchvision==0.26.0+cu128
if errorlevel 1 goto :fail
echo.
echo ======== 自检 ========
"%PY%" "%~dp0check_torch.py"
if errorlevel 1 goto :fail
echo.
echo [成功] 上面 CUDA 可用 应为 True。如果还是 False, 把整个窗口截图发我。
pause
exit /b 0
:fail
echo [失败] 把整个窗口截图发我。
pause
exit /b 1
