#!/usr/bin/env bash
# Render.com build script

set -o errexit  # exit on error

# Set production settings
export DJANGO_SETTINGS_MODULE=piticas_distribuicao.settings_render

# Install dependencies (try production first, fallback to basic)
if pip install -r requirements-production.txt; then
    echo "✅ Instalação com PostgreSQL concluída"
else
    echo "⚠️ Erro com PostgreSQL, usando versão básica"
    pip install -r requirements.txt
fi

# Collect static files
python manage.py collectstatic --noinput

# Run migrations
python manage.py migrate

# Setup for Render deployment
python setup_render.py
