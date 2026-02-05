@echo off
echo ===================================================
echo   LAUNCHING FOOSEE CHEMICAL EQUIPMENT VISUALIZER
echo ===================================================

echo [1/3] Starting Django Backend (Port 8000)...
start "FOOSEE Backend" cmd /k "cd backend && venv\Scripts\python manage.py runserver 127.0.0.1:8000"

echo Waiting 5 seconds for backend to warm up...
timeout /t 5 /nobreak > nul

echo [2/3] Starting React Web Frontend (Port 3000)...
start "FOOSEE Web" cmd /k "cd web-frontend && npm start"

echo [3/3] Starting Desktop Application...
start "FOOSEE Desktop" cmd /k "cd desktop-app && ..\backend\venv\Scripts\python main.py"

echo ===================================================
echo   SYSTEM LAUNCHED!
echo ===================================================
echo.
echo 1. Web App: http://localhost:3000
echo 2. Login with: admin / admin
echo.
pause
