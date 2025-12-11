# Django Scheduling App

A full-featured scheduling application built with Django.

## Features
- Event scheduling and management
- User authentication and profiles
- Event sharing and connections
- Group events
- Recurring events
- Notifications and reminders
- Event categories

## Local Development

### Prerequisites
- Python 3.11+
- pip

### Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run migrations:
```bash
python manage.py migrate
```

3. Create a superuser:
```bash
python manage.py createsuperuser
```

4. Run the development server:
```bash
python manage.py runserver
```

5. Visit `http://127.0.0.1:8000` in your browser

## Deployment

See [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for detailed instructions on deploying to free hosting platforms like Render, Railway, or PythonAnywhere.

## Project Structure

```
scheduling_app/
├── schedules/              # Main app
│   ├── migrations/         # Database migrations
│   ├── models.py          # Data models
│   ├── views.py           # View logic
│   ├── forms.py           # Forms
│   └── urls.py            # URL routing
├── scheduling_app/         # Project settings
│   ├── settings.py        # Django settings
│   ├── urls.py            # Main URL config
│   └── templates/         # HTML templates
├── manage.py              # Django management script
└── requirements.txt       # Python dependencies
```

## Technologies Used
- Django 5.1
- SQLite (development) / PostgreSQL (production recommended)
- OpenAI API (for AI features)
- WhiteNoise (static file serving)
- Gunicorn (production server)

## Notes
- The `django-q` task queue is currently disabled due to compatibility issues with Django 5.1
- For production deployment, consider using PostgreSQL instead of SQLite
- Make sure to set proper environment variables for production (see DEPLOYMENT_GUIDE.md)
