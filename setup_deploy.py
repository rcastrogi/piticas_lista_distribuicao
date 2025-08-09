#!/usr/bin/env python
"""
Script para configurar deploy da aplicação Piticas
"""
import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'piticas_distribuicao.settings')
django.setup()

from django.contrib.auth.models import User
from django.core.management import execute_from_command_line

def setup_for_deployment():
    """Configura a aplicação para deploy"""
    print("🚀 Configurando aplicação para deploy...")
    
    # Executar migrações
    print("📊 Executando migrações...")
    execute_from_command_line(['manage.py', 'migrate'])
    
    # Coletar arquivos estáticos
    print("📁 Coletando arquivos estáticos...")
    execute_from_command_line(['manage.py', 'collectstatic', '--noinput'])
    
    # Criar superusuário se não existir
    print("👤 Verificando superusuário...")
    if not User.objects.filter(is_superuser=True).exists():
        print("Criando usuário admin...")
        User.objects.create_superuser(
            username='admin',
            email='admin@piticas.com',
            password='admin123'
        )
        print("✅ Usuário admin criado (username: admin, password: admin123)")
    else:
        print("✅ Superusuário já existe")
    
    # Executar script de população se o banco estiver vazio
    print("🗃️ Verificando dados de exemplo...")
    from distribuicao.models import Grade
    if not Grade.objects.exists():
        print("Criando dados de exemplo...")
        os.system('python populate_db.py')
        print("✅ Dados de exemplo criados")
    else:
        print("✅ Dados já existem")
    
    print("🎉 Aplicação configurada com sucesso!")
    print("📋 Credenciais para demonstração:")
    print("   - URL Admin: /admin/")
    print("   - Username: admin")
    print("   - Password: admin123")

if __name__ == "__main__":
    setup_for_deployment()
