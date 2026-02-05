@echo off
echo ====================================
echo Chemical Equipment Visualizer
echo Starting All Services...
echo ====================================
echo.

REM Start Django Backend
echo [1/3] Starting Django Backend...
start "Django Backend" cmd /k "cd backend && python -m venv venv && venv\Scripts\activate && pip install -r requirements.txt && python manage.py migrate && python manage.py runserver"

timeout /t 5

REM Start React Frontend
echo [2/3] Starting React Frontend...
start "React Frontend" cmd /k "cd web-frontend && npm install && npm start"

timeout /t 3

REM Instructions for Desktop App
echo [3/3] Desktop App Instructions:
echo.
echo To run the desktop app, open a new terminal and run:
echo   cd desktop-app
echo   python -m venv venv
echo   venv\Scripts\activate
echo   pip install -r requirements.txt
echo   python main.py
echo.
echo ====================================
echo All services starting...
echo ====================================
echo.
echo Backend: http://localhost:8000
echo Web App: http://localhost:3000
echo Desktop: Run manually (see above)
echo.
echo Press any key to exit this launcher...
pause > nul
