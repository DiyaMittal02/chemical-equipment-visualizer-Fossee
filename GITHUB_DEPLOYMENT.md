# 🚀 GitHub Deployment Guide

## Step 1: Create GitHub Repository

1. Go to [GitHub](https://github.com/) and log in
2. Click the **"+"** icon → **"New repository"**
3. Fill in:
   - **Repository name**: `chemical-equipment-visualizer` (or your choice)
   - **Description**: "Full-stack chemical equipment data analysis tool"
   - **Visibility**: Public or Private
   - **DO NOT** initialize with README, .gitignore, or license (we already have these)
4. Click **"Create repository"**

## Step 2: Initialize Git & Push to GitHub

Open PowerShell in the project directory (`C:\Users\lenovo\OneDrive\Desktop\FOOSEE`) and run:

```powershell
# Initialize git repository
git init

# Add all files
git add .

# Create first commit
git commit -m "Initial commit: Chemical Equipment Visualizer"

# Add GitHub remote (replace YOUR_USERNAME and REPO_NAME)
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Example (replace with your details):
```powershell
git remote add origin https://github.com/johndoe/chemical-equipment-visualizer.git
git push -u origin main
```

## Step 3: Verify Upload

1. Go to your GitHub repository URL
2. Verify all files are uploaded
3. Check that the README displays properly

## 📋 Quick Commands Reference

```powershell
# Check git status
git status

# Add specific files
git add filename.txt

# Commit changes
git commit -m "Your commit message"

# Push changes
git push

# Pull latest changes
git pull
```

## 🔐 Authentication

If GitHub asks for credentials:

**Option 1: Personal Access Token (Recommended)**
1. Go to GitHub → Settings → Developer settings → Personal access tokens
2. Generate new token (classic)
3. Select scopes: `repo` (full control)
4. Copy the token
5. Use token as password when pushing

**Option 2: GitHub CLI**
```powershell
# Install GitHub CLI
winget install GitHub.cli

# Authenticate
gh auth login

# Follow prompts
```

## 📝 Future Updates

When you make changes:

```powershell
git add .
git commit -m "Describe your changes"
git push
```

## 🌐 GitHub Pages (Optional - for React frontend only)

To deploy the React frontend to GitHub Pages:

1. Install gh-pages:
```powershell
cd web-frontend
npm install --save-dev gh-pages
```

2. Add to `package.json`:
```json
{
  "homepage": "https://YOUR_USERNAME.github.io/REPO_NAME",
  "scripts": {
    "predeploy": "npm run build",
    "deploy": "gh-pages -d build"
  }
}
```

3. Deploy:
```powershell
npm run deploy
```

**Note**: This only deploys the frontend. The backend needs separate hosting (Heroku, Railway, AWS, etc.)

## ✅ Done!

Your project is now on GitHub! Share the repository link with others or add it to your portfolio.
