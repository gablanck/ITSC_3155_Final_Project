# Django Scheduling App - Free Deployment Guide

Your app is now configured for deployment! Here are the best **FREE** hosting options:

---

## Option 1: Render.com (RECOMMENDED - Easiest)

**Free Tier:** 750 hours/month, sleeps after 15 min of inactivity

### Steps:

1. **Push your code to GitHub:**
   ```bash
   cd c:\Users\jcste\Documents\GitHub\ITSC_3155_Final_Project
   git add .
   git commit -m "Prepare for deployment"
   git push origin main
   ```

2. **Sign up at [Render.com](https://render.com)**

3. **Create a New Web Service:**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Select your repository

4. **Configure the service:**
   - **Name:** scheduling-app (or your choice)
   - **Region:** Choose closest to you
   - **Branch:** main
   - **Root Directory:** `scheduling_app`
   - **Runtime:** Python 3
   - **Build Command:** `./build.sh`
   - **Start Command:** `gunicorn scheduling_app.wsgi:application`

5. **Add Environment Variables:**
   - Click "Advanced" → "Add Environment Variable"
   - Add these:
     ```
     DEBUG=False
     SECRET_KEY=your-super-secret-key-here-change-this
     ALLOWED_HOSTS=.onrender.com
     ```

6. **Deploy:**
   - Click "Create Web Service"
   - Wait 5-10 minutes for deployment
   - Your app will be live at: `https://your-app-name.onrender.com`

---

## Option 2: Railway.app

**Free Tier:** $5 credit/month (usually enough for small apps)

### Steps:

1. **Push code to GitHub** (same as above)

2. **Sign up at [Railway.app](https://railway.app)**

3. **Create New Project:**
   - Click "New Project" → "Deploy from GitHub repo"
   - Select your repository

4. **Configure:**
   - Railway auto-detects Django
   - Add environment variables in Settings:
     ```
     DEBUG=False
     SECRET_KEY=your-super-secret-key-here
     ```

5. **Deploy:**
   - Railway automatically deploys
   - Get your URL from the deployment

---

## Option 3: PythonAnywhere

**Free Tier:** 1 web app, limited CPU

### Steps:

1. **Sign up at [PythonAnywhere.com](https://www.pythonanywhere.com)**

2. **Upload your code:**
   - Use "Files" tab to upload or
   - Clone from GitHub using Bash console

3. **Create Web App:**
   - Go to "Web" tab
   - Click "Add a new web app"
   - Choose "Manual configuration" → Python 3.10

4. **Configure WSGI:**
   - Edit the WSGI file to point to your app:
   ```python
   import sys
   import os
   
   path = '/home/yourusername/scheduling_app'
   if path not in sys.path:
       sys.path.append(path)
   
   os.environ['DJANGO_SETTINGS_MODULE'] = 'scheduling_app.settings'
   
   from django.core.wsgi import get_wsgi_application
   application = get_wsgi_application()
   ```

5. **Install dependencies:**
   - Open Bash console
   - Run: `pip install -r requirements.txt`

6. **Run migrations:**
   ```bash
   python manage.py migrate
   python manage.py collectstatic
   ```

7. **Reload web app** from the Web tab

---

## Option 4: Vercel (with limitations)

Vercel is primarily for frontend but can host Django with some configuration. Not recommended for this app due to database limitations.

---

## Important Notes:

### Database:
- All free tiers use SQLite by default
- **Render/Railway:** Database resets on each deploy (use PostgreSQL for persistence)
- **PythonAnywhere:** SQLite persists

### To use PostgreSQL (recommended for production):

1. Add to `requirements.txt`:
   ```
   psycopg2-binary>=2.9.0
   dj-database-url>=2.1.0
   ```

2. Update `settings.py`:
   ```python
   import dj_database_url
   
   DATABASES = {
       'default': dj_database_url.config(
           default='sqlite:///db.sqlite3',
           conn_max_age=600
       )
   }
   ```

3. Add `DATABASE_URL` environment variable in your hosting platform

### Create Admin User:

After deployment, create a superuser:
```bash
python manage.py createsuperuser
```

On Render/Railway, use their console/shell feature.

---

## Troubleshooting:

### Static files not loading:
```bash
python manage.py collectstatic --no-input
```

### Database errors:
```bash
python manage.py migrate
```

### Check logs:
- **Render:** View logs in dashboard
- **Railway:** Click on deployment → View logs
- **PythonAnywhere:** Error log in Web tab

---

## My Recommendation:

**Start with Render.com** - it's the easiest and most reliable free option for Django apps. The setup is straightforward and it handles most configuration automatically.

Good luck with your deployment! 🚀
