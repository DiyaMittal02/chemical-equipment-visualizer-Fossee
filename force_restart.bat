@echo off
echo Stopping all python processes...
taskkill /F /IM python.exe > nul 2>&1

echo Starting Backend Server...
cd backend
venv\Scripts\python manage.py runserver 127.0.0.1:8000
