@echo off
echo Stopping existing python processes...
taskkill /F /IM python.exe > nul 2>&1

echo Starting Django Server on 127.0.0.1:8000...
cd backend
python -m venv venv
call venv\Scripts\activate
python manage.py runserver 127.0.0.1:8000
