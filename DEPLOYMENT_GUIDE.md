# 🚀 Complete Deployment Guide

This guide will help you deploy your Chemical Equipment Visualizer to the internet for FREE!

## 🎯 Deployment Architecture

- **Backend**: Render.com (Django API + PostgreSQL)
- **Frontend**: Vercel.com (React app)
- **Cost**: $0 (Free tier for both)

---

## Part 1: Deploy Backend to Render

### Step 1: Prepare Settings

The `settings.py` needs production configuration. I've created `settings_prod.py` for you.

### Step 2: Push Changes to GitHub

```bash
cd C:\Users\lenovo\OneDrive\Desktop\FOOSEE
git add .
git commit -m "Add deployment configuration"
git push
```

### Step 3: Deploy on Render

1. **Go to [Render.com](https://render.com/)** and sign up (use GitHub login)

2. **Create PostgreSQL Database**:
   - Click "New +" → "PostgreSQL"
   - Name: `chemical-equipment-db`
   - Leave defaults → Click "Create Database"
   - **Copy the "Internal Database URL"** (you'll need this)

3. **Create Web Service**:
   - Click "New +" → "Web Service"
   - Connect your GitHub repository: `chemical-equipment-visualizer-Fossee`
   - Settings:
     - **Name**: `chemical-equipment-api`
     - **Region**: Choose closest to you
     - **Branch**: `main`
     - **Root Directory**: `backend`
     - **Runtime**: `Python 3`
     - **Build Command**: `sh build.sh`
     - **Start Command**: `gunicorn backend.wsgi:application`

4. **Environment Variables** (Click "Advanced" → "Add Environment Variable"):
   ```
   PYTHON_VERSION=3.11.0
   DATABASE_URL=[paste your PostgreSQL Internal URL]
   SECRET_KEY=your-secret-key-here-make-it-random
   DEBUG=False
   ALLOWED_HOSTS=.onrender.com
   ```

5. **Click "Create Web Service"**

6. Wait 5-10 minutes for build to complete

7. **Your backend will be live at**: `https://chemical-equipment-api.onrender.com`

### Step 4: Create Superuser

Once deployed, go to Render dashboard → Shell tab:
```bash
python manage.py createsuperuser
```

---

## Part 2: Deploy Frontend to Vercel

### Step 1: Update API URL

Before deploying, update the frontend to point to your Render backend:

Edit `web-frontend/src/api.js`:
```javascript
const API_BASE_URL = 'https://chemical-equipment-api.onrender.com/api';
// Replace with YOUR actual Render URL
```

Commit and push:
```bash
git add .
git commit -m "Update API URL for production"
git push
```

### Step 2: Deploy on Vercel

1. **Go to [Vercel.com](https://vercel.com/)** and sign up (use GitHub login)

2. **Import Project**:
   - Click "Add New" → "Project"
   - Select your repository: `chemical-equipment-visualizer-Fossee`
   - Click "Import"

3. **Configure Project**:
   - **Framework Preset**: Create React App
   - **Root Directory**: `web-frontend`
   - **Build Command**: `npm run build`
   - **Output Directory**: `build`

4. **Click "Deploy"**

5. Wait 2-3 minutes

6. **Your frontend will be live at**: `https://your-project.vercel.app`

---

## Part 3: Connect Frontend & Backend

### Update CORS on Backend

1. Go to Render dashboard → Your web service → Environment
2. Update `ALLOWED_HOSTS`:
   ```
   ALLOWED_HOSTS=.onrender.com,.vercel.app,localhost
   ```

3. Add new variable `CORS_ALLOWED_ORIGINS`:
   ```
   CORS_ALLOWED_ORIGINS=https://your-project.vercel.app,http://localhost:3000
   ```
   (Replace with your actual Vercel URL)

4. Redeploy the backend (it will auto-redeploy when you save env vars)

---

## 🧪 Testing Your Deployment

1. Visit your Vercel URL: `https://your-project.vercel.app`
2. Register a new account (or login with the superuser you created)
3. Upload `sample_equipment_data.csv`
4. Verify charts and PDF download work

---

## 🔒 Important: Secure Your Deployment

### Generate a Strong SECRET_KEY

Run this in Python:
```python
import secrets
print(secrets.token_urlsafe(50))
```

Use the output as your `SECRET_KEY` in Render environment variables.

---

## 📊 Free Tier Limits

**Render Free Tier**:
- ✓ 750 hours/month (enough for 1 service)
- ✓ PostgreSQL: 1GB storage, expires in 90 days
- ⚠️ Spins down after 15 minutes of inactivity (first request takes ~30 seconds)

**Vercel Free Tier**:
- ✓ Unlimited bandwidth
- ✓ 100 GB-hours compute
- ✓ Custom domain support

---

## 🎯 Custom Domain (Optional)

### For Vercel (Frontend):
1. Vercel Dashboard → Your project → Settings → Domains
2. Add your domain
3. Update DNS records as instructed

### For Render (Backend):
1. Render Dashboard → Your service → Settings → Custom Domain
2. Add your domain
3. Update DNS records

---

## 🐛 Troubleshooting

### Backend Issues:

**500 Error**:
- Check Render logs: Dashboard → Logs
- Verify `DATABASE_URL` is set correctly
- Ensure `DEBUG=False`

**Database Connection Error**:
- Verify PostgreSQL is running
- Check `DATABASE_URL` format

### Frontend Issues:

**API Connection Error**:
- Verify `api.js` has correct Render URL
- Check CORS settings on backend
- Open browser console (F12) for errors

**Build Failed**:
- Check Vercel build logs
- Verify `package.json` scripts are correct

---

## 📝 Deployment Checklist

- [ ] Push latest code to GitHub
- [ ] Create Render account
- [ ] Create PostgreSQL database on Render
- [ ] Deploy backend to Render
- [ ] Set environment variables on Render
- [ ] Create superuser on deployed backend
- [ ] Update `api.js` with Render URL
- [ ] Push updated frontend code
- [ ] Create Vercel account
- [ ] Deploy frontend to Vercel
- [ ] Update CORS settings on Render
- [ ] Test the live application
- [ ] Generate strong SECRET_KEY

---

## 🎉 Success!

Once deployed, share your links:
- **Live App**: `https://your-project.vercel.app`
- **API**: `https://chemical-equipment-api.onrender.com/api/`
- **GitHub**: `https://github.com/DiyaMittal02/chemical-equipment-visualizer-Fossee`

Add these to your portfolio, resume, or LinkedIn! 🚀
