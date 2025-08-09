#!/usr/bin/env python
"""
Script de configuração para PythonAnywhere
"""

import os
import sys

import django

# Configurar Django
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "piticas_distribuicao.settings_pythonanywhere"
)
django.setup()

from django.contrib.auth.models import User


def setup_pythonanywhere():
    """Configura a aplicação para PythonAnywhere"""
    print("🐍 Configurando para PythonAnywhere...")

    # Criar superusuário se não existir
    print("👤 Configurando usuário admin...")
    try:
        if not User.objects.filter(is_superuser=True).exists():
            User.objects.create_superuser(
                username="admin", email="admin@piticas.com", password="admin123"
            )
            print("✅ Usuário admin criado")
        else:
            print("✅ Usuário admin já existe")
    except Exception as e:
        print(f"⚠️ Erro ao criar usuário: {e}")

    # Verificar e criar dados de exemplo
    print("🗃️ Verificando dados de exemplo...")
    try:
        from distribuicao.models import Grade

        if not Grade.objects.exists():
            print("📊 Criando dados de exemplo...")
            # Executar populate_db
            import subprocess

            result = subprocess.run(
                [sys.executable, "populate_db.py"],
                capture_output=True,
                text=True,
                cwd=".",
            )
            if result.returncode == 0:
                print("✅ Dados de exemplo criados")
            else:
                print(f"⚠️ Aviso: {result.stderr}")
        else:
            print("✅ Dados já existem")
    except Exception as e:
        print(f"⚠️ Erro ao verificar dados: {e}")

    print("🎉 Configuração PythonAnywhere concluída!")
    print("🌐 Acesse /admin/ com:")
    print("   Username: admin")
    print("   Password: admin123")


if __name__ == "__main__":
    setup_pythonanywhere()
