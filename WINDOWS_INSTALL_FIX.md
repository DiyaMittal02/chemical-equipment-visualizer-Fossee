# Windows Installation Fix Guide

## Problem
The standard requirements.txt is failing to install on Windows because some packages (Pandas, ReportLab) require compilation.

## Solution Options

### Option 1: Use Pre-compiled Wheels (RECOMMENDED)

Install packages individually using pre-built wheels:

```bash
# Make sure you're in the backend directory with venv activated
cd backend
venv\Scripts\activate

# Install Django and DRF first
pip install Django==4.2.0
pip install djangorestframework==3.14.0
pip install django-cors-headers==4.0.0

# Install Pandas (this should get a pre-built wheel)
pip install pandas

# Install ReportLab  
pip install reportlab

# Install Pillow
pip install Pillow

# Save the working versions
pip freeze > requirements-working.txt
```

### Option 2: Install Microsoft C++ Build Tools

If you want to build from source:

1. Download and install **Microsoft C++ Build Tools**:
   https://visualstudio.microsoft.com/visual-cpp-build-tools/

2. Select "Desktop development with C++"

3. Then try: `pip install -r requirements.txt`

### Option 3: Use Anaconda/Miniconda (EASIEST)

Anaconda comes with pre-compiled scientific packages:

```bash
# Download Miniconda from https://docs.conda.io/en/latest/miniconda.html

# Create environment
conda create -n foosee python=3.11
conda activate foosee

# Install packages
conda install django djangorestframework pandas pillow
pip install django-cors-headers reportlab

# Navigate to backend
cd backend
python manage.py migrate
python manage.py runserver
```

### Option 4: Minimal Installation (For Testing)

If you just want to test the application quickly:

```bash
pip install Django==4.2.0 djangorestframework==3.14.0 django-cors-headers==4.0.0
```

Then temporarily comment out Pandas functionality in the code and use simpler CSV processing.

## Quick Fix Commands

Run these commands one by one in your backend directory:

```powershell
# Activate virtual environment
venv\Scripts\activate

# Clear any cached packages
pip cache purge

# Upgrade pip
python -m pip install --upgrade pip

# Install core Django packages
pip install Django djangorestframework django-cors-headers

# Try installing pandas with different method
pip install --only-binary :all: pandas || pip install pandas --no-cache-dir

# Install reportlab
pip install reportlab --no-cache-dir

# Install Pillow
pip install Pillow

# Verify installations
pip list

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start server
python manage.py runserver
```

## Alternative: Simpler Requirements

I've created `requirements-minimal.txt` that you can try:

```
Django
djangorestframework
django-cors-headers
```

This will install latest compatible versions and allow you to run the basic application.

## After Successful Installation

Once packages are installed:

1. Run migrations: `python manage.py migrate`
2. Create admin user: `python manage.py createsuperuser`
3. Start server: `python manage.py runserver`
4. Test at: http://localhost:8000/admin

## Still Having Issues?

If installation continues to fail, we can:
1. Modify the code to work without Pandas (use Python's csv module)
2. Modify the code to work without ReportLab (skip PDF generation)
3. Use Docker instead (I can provide a Dockerfile)

Let me know which solution works best for you!
