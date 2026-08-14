@echo off
cls
echo.
echo ========================================
echo 🗺️  Phuong Long Huong - Ban Do Ve Tinh
echo ========================================
echo.

REM Kiểm tra Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Loi: Python khong duoc cai dat
    echo    Vui long cai dat Python tu https://python.org
    echo    Chon "Add Python to PATH" trong qua trinh cai dat
    pause
    exit /b 1
)

echo ✓ Python da san sang
echo.

REM Chạy server
python server.py

pause
