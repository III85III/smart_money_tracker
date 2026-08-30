@echo off
cd /d "%~dp0"
title III85III - Setup & Run
color 0E
echo ==========================================
echo    Setting up Smart Money Tracker...
echo ==========================================
python --version >nul 2>&1
if %errorlevel% neq 0 (echo [ERROR] Python not found! Install Python first. & pause & exit /b)
echo [1/2] Installing dependencies...
python -m pip install --upgrade pip >nul 2>&1
if exist requirements.txt python -m pip install -r requirements.txt
echo [2/2] Launching...
call run.bat
pause