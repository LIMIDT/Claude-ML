@echo off
title PyTorch 自检
echo ======== PyTorch 环境自检 ========
echo.
"%USERPROFILE%\miniconda3\envs\ml\python.exe" "%~dp0check_torch.py"
echo.
if errorlevel 1 echo [失败] 把上面的内容截图发我。
if not errorlevel 1 echo [成功] 环境没问题, 可以去 VS Code 跑 01_mnist_quickstart.py 了。
echo.
pause
