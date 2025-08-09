#!/usr/bin/env bash
# Render.com build script

set -o errexit  # exit on error

# Set production settings
export DJANGO_SETTINGS_MODULE=piticas_distribuicao.settings_render

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Run migrations
python manage.py migrate

# Setup for Render deployment
python setup_render.py
