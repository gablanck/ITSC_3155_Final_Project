#!/usr/bin/env bash
# exit on error
set -o errexit

# Upgrade pip and setuptools first
pip install --upgrade pip setuptools wheel

# Install dependencies
pip install -r requirements.txt

# Change to Django project directory
cd scheduling_app

# Collect static files
python manage.py collectstatic --no-input

# Run migrations
python manage.py migrate
