@echo off
echo ===========================================
echo   FULL SYSTEM RESTART (WEB + BACKEND)
echo ===========================================

echo [1/3] Stopping all processes (Node + Python)...
taskkill /F /IM node.exe > nul 2>&1
taskkill /F /IM python.exe > nul 2>&1

echo [2/3] Starting Backend...
start "FOOSEE Backend" cmd /k "cd backend && venv\Scripts\python manage.py runserver 127.0.0.1:8000"

echo Waiting 5 seconds...
timeout /t 5 /nobreak > nul

echo [3/3] Starting Web Frontend...
start "FOOSEE Web" cmd /k "cd web-frontend && npm start"

echo.
echo DONE!
echo Please wait for the browser to open.
echo Login with: admin / admin
pause
