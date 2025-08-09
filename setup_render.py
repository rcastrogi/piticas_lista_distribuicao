#!/usr/bin/env python
"""
Script específico para configuração no Render.com
"""
import os
import sys
import django

# Detectar se estamos no Render (ou qualquer ambiente de produção)
if 'RENDER' in os.environ or 'DATABASE_URL' in os.environ:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'piticas_distribuicao.settings_render')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'piticas_distribuicao.settings')

django.setup()

from django.contrib.auth.models import User
from django.core.management import execute_from_command_line

def setup_for_render():
    """Configura a aplicação especificamente para Render"""
    print("🎨 Configurando para Render.com...")
    
    # Criar superusuário se não existir
    print("👤 Configurando usuário admin...")
    try:
        if not User.objects.filter(is_superuser=True).exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@piticas.com',
                password='admin123'
            )
            print("✅ Usuário admin criado")
        else:
            print("✅ Usuário admin já existe")
    except Exception as e:
        print(f"⚠️ Erro ao criar usuário: {e}")
    
    # Executar script de população se necessário
    print("🗃️ Verificando dados de exemplo...")
    try:
        from distribuicao.models import Grade
        if not Grade.objects.exists():
            print("📊 Criando dados de exemplo...")
            # Import e execute o populate_db
            import subprocess
            result = subprocess.run([sys.executable, 'populate_db.py'], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                print("✅ Dados de exemplo criados")
            else:
                print(f"⚠️ Erro ao criar dados: {result.stderr}")
        else:
            print("✅ Dados já existem")
    except Exception as e:
        print(f"⚠️ Erro ao verificar dados: {e}")
    
    print("🎉 Configuração para Render concluída!")
    print("🔗 Acesse /admin/ com:")
    print("   Username: admin")
    print("   Password: admin123")

if __name__ == "__main__":
    setup_for_render()
