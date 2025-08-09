#!/bin/bash
# Script de comandos para PythonAnywhere Console

echo "🐍 Configurando projeto no PythonAnywhere..."

# Navegar para o diretório
cd piticas-lista-distribuicao

echo "📦 Instalando dependências..."
pip3.10 install --user Django==5.2.5
pip3.10 install --user Pillow==10.4.0
pip3.10 install --user django-crispy-forms==2.3
pip3.10 install --user crispy-bootstrap5==2024.2
pip3.10 install --user whitenoise==6.8.2

echo "🗃️ Configurando banco de dados..."
python3.10 manage.py migrate --settings=piticas_distribuicao.settings_pythonanywhere

echo "👤 Criando usuário admin e dados..."
python3.10 setup_pythonanywhere.py

echo "📁 Coletando arquivos estáticos..."
python3.10 manage.py collectstatic --noinput --settings=piticas_distribuicao.settings_pythonanywhere

echo "✅ Configuração concluída!"
echo "🌐 Agora vá para Web tab e click em Reload"
