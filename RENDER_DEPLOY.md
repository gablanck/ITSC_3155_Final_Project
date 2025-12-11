# Quick Render Deployment Instructions

## Files are now in the correct location!

All deployment files are now in the **root directory** of your repository.

## Steps to Deploy on Render:

### 1. Push your changes to GitHub:
```bash
cd c:\Users\jcste\Documents\GitHub\ITSC_3155_Final_Project
git add .
git commit -m "Add deployment files to root"
git push origin main
```

### 2. Configure Render:

Go to your Render dashboard and update your service settings:

**Build & Deploy Settings:**
- **Root Directory:** Leave EMPTY (or just `/`)
- **Build Command:** `./build.sh`
- **Start Command:** `cd scheduling_app && gunicorn scheduling_app.wsgi:application`

**Environment Variables:**
Add these in the "Environment" tab:
```
DEBUG=False
SECRET_KEY=your-super-secret-random-key-here-change-this
ALLOWED_HOSTS=.onrender.com
```

### 3. Deploy:
- Click "Manual Deploy" → "Deploy latest commit"
- Wait 5-10 minutes
- Your app will be live!

## Alternative: Use render.yaml (Easier)

I've created a `render.yaml` file. Render will automatically detect it and configure everything for you!

Just push to GitHub and Render will handle the rest.

## Troubleshooting:

### If build fails:
1. Check the build logs in Render dashboard
2. Make sure `build.sh` has execute permissions (Render usually handles this)
3. Verify all environment variables are set

### If app doesn't start:
1. Check the logs in Render dashboard
2. Make sure `ALLOWED_HOSTS` includes your Render domain
3. Verify `DEBUG=False` is set

### After successful deployment:
1. Visit your app URL
2. Go to `/admin` to access Django admin
3. Create a superuser using Render's shell:
   ```bash
   cd scheduling_app
   python manage.py createsuperuser
   ```

## Your app structure:
```
ITSC_3155_Final_Project/          ← Root (where Render looks)
├── requirements.txt              ← Dependencies
├── build.sh                      ← Build script
├── Procfile                      ← Start command
├── runtime.txt                   ← Python version
├── render.yaml                   ← Render config (optional)
└── scheduling_app/               ← Django project
    ├── manage.py
    ├── schedules/
    └── scheduling_app/
```

Good luck! 🚀
