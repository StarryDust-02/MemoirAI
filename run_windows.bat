@echo off
setlocal

echo Checking for Python 3...

python --version >nul 2>&1
if %errorlevel% == 0 (
    echo Python detected. Running main.py...
    python main.py
    pause
    exit /b
)

py --version >nul 2>&1
if %errorlevel% == 0 (
    echo Python detected via py launcher. Running main.py...
    py main.py
    pause
    exit /b
)

echo Python not found.

echo Attempting to run bundled installer: python-3.14.6-amd64.exe

if exist "python-3.14.6-amd64.exe" (
    start "" "python-3.14.6-amd64.exe"
    echo Installer launched. Please install Python and re-run this script.
    pause
    exit /b
)

echo ERROR: Python installer not found in project root.
pause
exit /b
