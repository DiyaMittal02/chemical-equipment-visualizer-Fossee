@echo off
echo ===========================================
echo   FOOSEE REPAIR SCRIPT - ONCE AND FOR ALL
echo ===========================================

echo [1/5] Stopping all python processes...
taskkill /F /IM python.exe > nul 2>&1

echo [2/5] Cleaning environment...
cd backend
if exist "venv" rmdir /s /q "venv"
if exist "db.sqlite3" del "db.sqlite3"

echo [3/5] Installing STABLE dependencies...
python -m venv venv
call venv\Scripts\activate
python -m pip install --upgrade pip
pip install Django==4.2.7 djangorestframework==3.14.0 django-cors-headers==4.0.0 pandas==2.0.3 reportlab==4.0.4 Pillow==10.0.0

echo [4/5] Setting up database...
python manage.py makemigrations
python manage.py migrate
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell

echo [5/5] Starting Server on 127.0.0.1:8000...
echo.
echo SERVER IS RUNNING. DO NOT CLOSE THIS WINDOW.
echo.
python manage.py runserver 127.0.0.1:8000
