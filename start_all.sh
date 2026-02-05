#!/bin/bash

echo "===================================="
echo "Chemical Equipment Visualizer"
echo "Starting All Services..."
echo "===================================="
echo ""

# Start Django Backend
echo "[1/3] Starting Django Backend..."
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver &
BACKEND_PID=$!
cd ..

sleep 5

# Start React Frontend
echo "[2/3] Starting React Frontend..."
cd web-frontend
npm install
npm start &
FRONTEND_PID=$!
cd ..

sleep 3

# Instructions for Desktop App
echo "[3/3] Desktop App Instructions:"
echo ""
echo "To run the desktop app, open a new terminal and run:"
echo "  cd desktop-app"
echo "  python3 -m venv venv"
echo "  source venv/bin/activate"
echo "  pip install -r requirements.txt"
echo "  python main.py"
echo ""
echo "===================================="
echo "All services started!"
echo "===================================="
echo ""
echo "Backend: http://localhost:8000"
echo "Web App: http://localhost:3000"
echo "Desktop: Run manually (see above)"
echo ""
echo "Press Ctrl+C to stop all services"

# Wait and cleanup on exit
trap "kill $BACKEND_PID $FRONTEND_PID; exit" INT
wait
