@echo off
setlocal
title PyTorch 环境一键安装
set "CONDA_ROOT=%USERPROFILE%\miniconda3"
set "ENV_NAME=ml"
set "PYVER=3.11"
set "TORCH_MIRROR=https://mirrors.aliyun.com/pytorch-wheels"
set "PIP_MIRROR=https://mirrors.aliyun.com/pypi/simple/"
echo ============================================
echo   PyTorch 环境一键安装  环境名 %ENV_NAME%
echo ============================================
echo.

if exist "%CONDA_ROOT%\Scripts\conda.exe" goto :have_conda
echo [1/4] 没找到 Miniconda, 开始下载安装...
set "INST=%TEMP%\Miniconda3-latest-Windows-x86_64.exe"
if exist "%INST%" goto :run_inst
curl -L -o "%INST%" https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-latest-Windows-x86_64.exe
if exist "%INST%" goto :run_inst
echo 清华源下载失败, 换官方源重试...
curl -L -o "%INST%" https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe
if not exist "%INST%" goto :e_download
:run_inst
echo 正在静默安装 Miniconda 到 %CONDA_ROOT%  约 1-3 分钟, 请等待...
start /wait "" "%INST%" /InstallationType=JustMe /AddToPath=0 /RegisterPython=0 /S /D=%CONDA_ROOT%
if not exist "%CONDA_ROOT%\Scripts\conda.exe" goto :e_install
echo Miniconda 安装完成。
goto :have_conda

:have_conda
echo [1/4] Miniconda 就绪: %CONDA_ROOT%
call "%CONDA_ROOT%\Scripts\activate.bat" "%CONDA_ROOT%"
echo 配置镜像源并接受服务条款...
call conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/main >nul 2>nul
call conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/r >nul 2>nul
call conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/msys2 >nul 2>nul
call conda config --remove channels defaults >nul 2>nul
call conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2 >nul 2>nul
call conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r >nul 2>nul
call conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main >nul 2>nul
call conda config --set show_channel_urls yes >nul 2>nul
call conda config --set auto_activate_base false >nul 2>nul
echo.

echo [2/4] 创建环境 %ENV_NAME%  Python %PYVER%
if exist "%CONDA_ROOT%\envs\%ENV_NAME%\python.exe" goto :env_ok
call conda create -y -n %ENV_NAME% python=%PYVER% --override-channels -c https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
if not exist "%CONDA_ROOT%\envs\%ENV_NAME%\python.exe" goto :e_env
:env_ok
set "PY=%CONDA_ROOT%\envs\%ENV_NAME%\python.exe"
echo 环境就绪: %PY%
echo.

echo [3/4] 检测显卡并安装 PyTorch
set "FLAVOR=cpu"
where nvidia-smi >nul 2>nul
if errorlevel 1 goto :do_torch
nvidia-smi >nul 2>nul
if errorlevel 1 goto :do_torch
set "FLAVOR=cu128"
echo 检测到 NVIDIA 显卡, 安装 CUDA 12.8 版本。
:do_torch
if "%FLAVOR%"=="cpu" echo 未检测到 NVIDIA 显卡, 安装 CPU 版本。
"%PY%" -m pip install -i %PIP_MIRROR% --upgrade pip
if "%FLAVOR%"=="cpu" "%PY%" -m pip install -i %PIP_MIRROR% torch torchvision
if "%FLAVOR%"=="cu128" "%PY%" -m pip install -i %PIP_MIRROR% -f %TORCH_MIRROR%/cu128 torch==2.11.0+cu128 torchvision==0.26.0+cu128
if errorlevel 1 goto :e_torch
echo.

echo [4/4] 安装常用库
"%PY%" -m pip install -i %PIP_MIRROR% numpy pandas matplotlib tqdm scikit-learn jupyter ipykernel
"%PY%" -m ipykernel install --user --name %ENV_NAME% --display-name "Python (%ENV_NAME%)" >nul 2>nul
echo.

echo ============ 自检 ============
"%PY%" "%~dp0check_torch.py"
if errorlevel 1 goto :e_check
echo.
echo 全部完成。
echo 下一步: 用 VS Code 打开本文件夹, Ctrl+Shift+P 输入 Python: Select Interpreter
echo          选 Python %PYVER% ^('%ENV_NAME%'^)  然后按 F5 运行 01_mnist_quickstart.py
echo.
pause
exit /b 0

:e_download
echo [失败] Miniconda 下载失败。请手动下载后放到 %TEMP% 再运行本脚本:
echo https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-latest-Windows-x86_64.exe
pause
exit /b 1
:e_install
echo [失败] Miniconda 安装失败。请手动双击 %INST% 安装到 %CONDA_ROOT% 后重跑。
pause
exit /b 1
:e_env
echo [失败] conda 环境创建失败, 把上面的报错截图给我。
pause
exit /b 1
:e_torch
echo [失败] PyTorch 安装失败, 把上面的报错截图给我。
pause
exit /b 1
:e_check
echo [失败] 自检没通过, 把上面的输出截图给我。
pause
exit /b 1
