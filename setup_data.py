import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "piticas_distribuicao.settings")
django.setup()

from django.contrib.auth.models import User

from distribuicao.models import (
    Consultor,
    Grade,
    ItemPackGrade,
    Licenca,
    ListaDistribuicao,
    Loja,
    PackGrade,
    Produto,
)

print("🚀 Iniciando população do banco de dados...")

# Verificar se já existe superusuário
if not User.objects.filter(is_superuser=True).exists():
    User.objects.create_superuser("admin", "admin@piticas.com", "admin123")
    print("✅ Superusuário 'admin' criado (senha: admin123)")
else:
    print("ℹ️ Superusuário já existe")

# Criar Grades
print("📐 Criando Grades...")
grade_juvenil, _ = Grade.objects.get_or_create(
    codigo="JUV", defaults={"descricao": "Grade Juvenil"}
)
grade_adulto, _ = Grade.objects.get_or_create(
    codigo="ADT", defaults={"descricao": "Grade Adulto"}
)
grade_infantil, _ = Grade.objects.get_or_create(
    codigo="INF", defaults={"descricao": "Grade Infantil"}
)

# Criar Licenças
print("🏷️ Criando Licenças...")
licenca_disney, _ = Licenca.objects.get_or_create(
    codigo="DIS", defaults={"descricao": "Disney"}
)
licenca_marvel, _ = Licenca.objects.get_or_create(
    codigo="MAR", defaults={"descricao": "Marvel"}
)
licenca_princesas, _ = Licenca.objects.get_or_create(
    codigo="PRI", defaults={"descricao": "Princesas Disney"}
)

# Criar Consultores
print("👥 Criando Consultores...")
consultor1, _ = Consultor.objects.get_or_create(
    codigo="C001", defaults={"nome": "Ana Silva"}
)
consultor2, _ = Consultor.objects.get_or_create(
    codigo="C002", defaults={"nome": "Carlos Santos"}
)
consultor3, _ = Consultor.objects.get_or_create(
    codigo="C003", defaults={"nome": "Maria Oliveira"}
)

# Criar usuários para lojas
print("🔐 Criando usuários de loja...")
user_sp, _ = User.objects.get_or_create(
    username="loja_sp001",
    defaults={
        "email": "sp001@piticas.com",
        "first_name": "Loja",
        "last_name": "São Paulo",
    },
)
user_sp.set_password("loja123")
user_sp.save()

user_rj, _ = User.objects.get_or_create(
    username="loja_rj001",
    defaults={
        "email": "rj001@piticas.com",
        "first_name": "Loja",
        "last_name": "Rio de Janeiro",
    },
)
user_rj.set_password("loja123")
user_rj.save()

# Criar Lojas
print("🏪 Criando Lojas...")
loja_sp, _ = Loja.objects.get_or_create(
    codigo="SP001", defaults={"descricao": "São Paulo - Centro", "usuario": user_sp}
)
loja_sp.consultores.add(consultor1, consultor2)

loja_rj, _ = Loja.objects.get_or_create(
    codigo="RJ001",
    defaults={"descricao": "Rio de Janeiro - Copacabana", "usuario": user_rj},
)
loja_rj.consultores.add(consultor2, consultor3)

# Criar Packs de Grade
print("📦 Criando Packs de Grade...")

# Pack Juvenil
pack_juvenil, created = PackGrade.objects.get_or_create(
    grade=grade_juvenil, nome="Pack Padrão Juvenil"
)
if created:
    ItemPackGrade.objects.create(pack_grade=pack_juvenil, tamanho="10", quantidade=1)
    ItemPackGrade.objects.create(pack_grade=pack_juvenil, tamanho="12", quantidade=2)
    ItemPackGrade.objects.create(pack_grade=pack_juvenil, tamanho="14", quantidade=2)
    ItemPackGrade.objects.create(pack_grade=pack_juvenil, tamanho="16", quantidade=1)

# Pack Adulto
pack_adulto, created = PackGrade.objects.get_or_create(
    grade=grade_adulto, nome="Pack Padrão Adulto"
)
if created:
    ItemPackGrade.objects.create(pack_grade=pack_adulto, tamanho="P", quantidade=2)
    ItemPackGrade.objects.create(pack_grade=pack_adulto, tamanho="M", quantidade=3)
    ItemPackGrade.objects.create(pack_grade=pack_adulto, tamanho="G", quantidade=2)
    ItemPackGrade.objects.create(pack_grade=pack_adulto, tamanho="GG", quantidade=1)

# Criar Produtos
print("👕 Criando Produtos...")
produto1, _ = Produto.objects.get_or_create(
    codigo="DIS001",
    defaults={
        "descricao": "Camiseta Mickey Mouse",
        "licenca": licenca_disney,
        "pack_grade": pack_juvenil,
        "preco_unitario": 29.90,
    },
)

produto2, _ = Produto.objects.get_or_create(
    codigo="MAR001",
    defaults={
        "descricao": "Camiseta Homem Aranha",
        "licenca": licenca_marvel,
        "pack_grade": pack_adulto,
        "preco_unitario": 39.90,
    },
)

produto3, _ = Produto.objects.get_or_create(
    codigo="PRI001",
    defaults={
        "descricao": "Vestido Elsa Frozen",
        "licenca": licenca_princesas,
        "pack_grade": pack_juvenil,
        "preco_unitario": 49.90,
    },
)

# Criar Listas de Distribuição
print("📋 Criando Listas de Distribuição...")

ListaDistribuicao.objects.get_or_create(
    codigo="JAN2025-SP001-DIS001",
    defaults={
        "mes": 1,
        "ano": 2025,
        "loja": loja_sp,
        "produto": produto1,
        "quantidade_consultor": 10,
        "quantidade_loja": 5,
    },
)

ListaDistribuicao.objects.get_or_create(
    codigo="JAN2025-SP001-MAR001",
    defaults={
        "mes": 1,
        "ano": 2025,
        "loja": loja_sp,
        "produto": produto2,
        "quantidade_consultor": 8,
        "quantidade_loja": 4,
    },
)

ListaDistribuicao.objects.get_or_create(
    codigo="JAN2025-RJ001-PRI001",
    defaults={
        "mes": 1,
        "ano": 2025,
        "loja": loja_rj,
        "produto": produto3,
        "quantidade_consultor": 12,
        "quantidade_loja": 6,
    },
)

ListaDistribuicao.objects.get_or_create(
    codigo="FEV2025-SP001-PRI001",
    defaults={
        "mes": 2,
        "ano": 2025,
        "loja": loja_sp,
        "produto": produto3,
        "quantidade_consultor": 14,
        "quantidade_loja": 7,
    },
)

print("\n✅ Banco de dados populado com sucesso!")
print(f"📊 Estatísticas:")
print(f"   - {Grade.objects.count()} Grades")
print(f"   - {Licenca.objects.count()} Licenças")
print(f"   - {Consultor.objects.count()} Consultores")
print(f"   - {Loja.objects.count()} Lojas")
print(f"   - {Produto.objects.count()} Produtos")
print(f"   - {ListaDistribuicao.objects.count()} Listas de Distribuição")

print(f"\n🔐 Usuários de teste:")
print(f"   - admin / admin123 (administrador)")
print(f"   - loja_sp001 / loja123 (Loja São Paulo)")
print(f"   - loja_rj001 / loja123 (Loja Rio de Janeiro)")

print(f"\n🌐 Para acessar o sistema:")
print(f"   1. Execute: python manage.py runserver")
print(f"   2. Acesse: http://127.0.0.1:8000/")
print(f"   3. Admin: http://127.0.0.1:8000/admin/")
