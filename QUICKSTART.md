# Quick Start Guide

## Installation & Running

### Option 1: Windows Quick Start

1. **Backend**
```cmd
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

2. **Web Frontend** (New Terminal)
```cmd
cd web-frontend
npm install
npm start
```

3. **Desktop App** (New Terminal)
```cmd
cd desktop-app
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

### Option 2: Mac/Linux Quick Start

1. **Backend**
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

2. **Web Frontend** (New Terminal)
```bash
cd web-frontend
npm install
npm start
```

3. **Desktop App** (New Terminal)
```bash
cd desktop-app
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

## First Time Setup

1. Create a superuser for Django admin (optional):
```bash
cd backend
python manage.py createsuperuser
```

2. Test with sample data: Upload `sample_equipment_data.csv`

## Access Points

- **Django Backend**: http://localhost:8000
- **Django Admin**: http://localhost:8000/admin
- **React Web App**: http://localhost:3000
- **Desktop App**: Launch via `python main.py`

## Common Issues

### Port Already in Use
- Backend (8000): Change in `settings.py` or kill process
- React (3000): React will offer alternative port

### Module Not Found
- Ensure virtual environment is activated
- Re-run `pip install -r requirements.txt`

### CORS Errors
- Verify backend is running
- Check CORS settings in `backend/backend/settings.py`

## Testing Checklist

- [ ] Backend server starts without errors
- [ ] Can access admin panel
- [ ] React app loads successfully
- [ ] Desktop app launches
- [ ] Can register/login
- [ ] Can upload sample CSV
- [ ] Charts display correctly
- [ ] PDF download works
- [ ] History shows uploads

## Need Help?

Check the main README.md for detailed documentation.
