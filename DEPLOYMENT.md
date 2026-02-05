# Deployment Guide

## Backend Deployment (Django)

### Option 1: Render.com

1. Create account at https://render.com
2. Connect GitHub repository
3. Create new **Web Service**
4. Configure:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn backend.wsgi:application`
   - **Environment Variables**:
     ```
     PYTHON_VERSION=3.11
     SECRET_KEY=your-secret-key
     DEBUG=False
     ALLOWED_HOSTS=your-app.onrender.com
     ```

5. Add to `backend/requirements.txt`:
   ```
   gunicorn==21.2.0
   ```

6. Update `backend/backend/settings.py`:
   ```python
   import os
   
   SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-dev-key')
   DEBUG = os.environ.get('DEBUG', 'False') == 'True'
   ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')
   ```

### Option 2: Railway.app

1. Go to https://railway.app
2. Create new project from GitHub
3. Add PostgreSQL database (optional)
4. Set environment variables
5. Deploy

## Web Frontend Deployment (React)

### Option 1: Vercel

1. Install Vercel CLI: `npm install -g vercel`
2. Navigate to `web-frontend`
3. Run `vercel`
4. Update API URL in `.env.production`:
   ```
   REACT_APP_API_URL=https://your-backend.onrender.com/api
   ```

### Option 2: Netlify

1. Build project: `npm run build`
2. Create account at https://netlify.com
3. Drag and drop `build` folder
4. Or connect GitHub repo for auto-deployment

### Update CORS

In `backend/backend/settings.py`:
```python
CORS_ALLOWED_ORIGINS = [
    'https://your-frontend.vercel.app',
    'https://your-frontend.netlify.app',
]
```

## Desktop App Distribution

### Windows

1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```

2. Create executable:
   ```bash
   pyinstaller --name="EquipmentVisualizer" --windowed --onefile main.py
   ```

3. Distribute `dist/EquipmentVisualizer.exe`

### macOS

1. Use `py2app`:
   ```bash
   pip install py2app
   python setup.py py2app
   ```

2. Create DMG with `create-dmg`

### Linux

1. Create executable with PyInstaller
2. Or package as AppImage

## Production Checklist

### Backend
- [ ] Set proper SECRET_KEY
- [ ] Disable DEBUG
- [ ] Configure ALLOWED_HOSTS
- [ ] Set up database (PostgreSQL recommended)
- [ ] Configure static files
- [ ] Set up HTTPS
- [ ] Configure CORS properly
- [ ] Add rate limiting

### Frontend (Web)
- [ ] Build production bundle
- [ ] Update API URLs
- [ ] Enable HTTPS
- [ ] Add error tracking (Sentry)
- [ ] Configure CDN (optional)

### Desktop App
- [ ] Update API base URL to production
- [ ] Code signing (Windows/macOS)
- [ ] Create installer
- [ ] Test on clean system

## Monitoring

### Recommended Tools
- **Backend**: Sentry for error tracking
- **Frontend**: Google Analytics, Sentry
- **Uptime**: UptimeRobot
- **Performance**: New Relic, DataDog

## SSL/HTTPS

Both Render and Vercel provide free SSL certificates automatically.

For custom domains:
1. Configure DNS settings
2. Add custom domain in platform settings
3. Wait for SSL provisioning (automatic)

## Environment Variables Summary

### Backend (.env)
```
SECRET_KEY=your-long-random-secret-key
DEBUG=False
ALLOWED_HOSTS=your-domain.com,www.your-domain.com
DATABASE_URL=postgresql://user:pass@host:5432/dbname
CORS_ALLOWED_ORIGINS=https://your-frontend.com
```

### Frontend (.env.production)
```
REACT_APP_API_URL=https://your-backend.com/api
```

### Desktop (config.py)
```python
API_BASE_URL = "https://your-backend.com/api"
```

## Cost Estimate

### Free Tier Options
- **Render**: Free tier available
- **Railway**: $5 credit (trial)
- **Vercel**: Unlimited for personal
- **Netlify**: 100GB bandwidth/month

### Recommended Paid (If needed)
- **Render**: $7/month (starter)
- **Database**: Railway PostgreSQL $5/month
- **Domain**: $10-15/year (optional)

Total: ~$12-22/month (if paid hosting needed)

---

**Quick Deploy Commands**

```bash
# Build and deploy web frontend
cd web-frontend
npm run build
vercel --prod

# Deploy to Render (via GitHub integration)
git push origin main
# Render auto-deploys
```
