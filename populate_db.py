#!/usr/bin/env python
"""
Script para popular o banco de dados com dados de exemplo
Execute: python manage.py shell < populate_db.py
"""

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

# Criar Grades
print("Criando Grades...")
grade_juvenil, created = Grade.objects.get_or_create(
    codigo="JUV", defaults={"descricao": "Grade Juvenil"}
)

grade_adulto, created = Grade.objects.get_or_create(
    codigo="ADT", defaults={"descricao": "Grade Adulto"}
)

grade_infantil, created = Grade.objects.get_or_create(
    codigo="INF", defaults={"descricao": "Grade Infantil"}
)

# Criar Licenças
print("Criando Licenças...")
licenca_disney, created = Licenca.objects.get_or_create(
    codigo="DIS", defaults={"descricao": "Disney"}
)

licenca_marvel, created = Licenca.objects.get_or_create(
    codigo="MAR", defaults={"descricao": "Marvel"}
)

licenca_princesas, created = Licenca.objects.get_or_create(
    codigo="PRI", defaults={"descricao": "Princesas Disney"}
)

# Criar Consultores
print("Criando Consultores...")
consultor1, created = Consultor.objects.get_or_create(
    codigo="C001", defaults={"nome": "Ana Silva"}
)

consultor2, created = Consultor.objects.get_or_create(
    codigo="C002", defaults={"nome": "Carlos Santos"}
)

consultor3, created = Consultor.objects.get_or_create(
    codigo="C003", defaults={"nome": "Maria Oliveira"}
)

consultor4, created = Consultor.objects.get_or_create(
    codigo="C004", defaults={"nome": "João Pedro"}
)

# Criar usuários para as lojas
print("Criando usuários para as lojas...")
user_sp001, created = User.objects.get_or_create(
    username="loja_sp001",
    defaults={
        "email": "sp001@piticas.com",
        "first_name": "Loja",
        "last_name": "São Paulo Centro",
    },
)
if created:
    user_sp001.set_password("loja123")
    user_sp001.save()

user_rj001, created = User.objects.get_or_create(
    username="loja_rj001",
    defaults={
        "email": "rj001@piticas.com",
        "first_name": "Loja",
        "last_name": "Rio de Janeiro Copacabana",
    },
)
if created:
    user_rj001.set_password("loja123")
    user_rj001.save()

user_mg001, created = User.objects.get_or_create(
    username="loja_mg001",
    defaults={
        "email": "mg001@piticas.com",
        "first_name": "Loja",
        "last_name": "Belo Horizonte Centro",
    },
)
if created:
    user_mg001.set_password("loja123")
    user_mg001.save()

# Criar Lojas
print("Criando Lojas...")
loja_sp, created = Loja.objects.get_or_create(
    codigo="SP001", defaults={"descricao": "São Paulo - Centro", "usuario": user_sp001}
)
loja_sp.consultores.add(consultor1, consultor2)

loja_rj, created = Loja.objects.get_or_create(
    codigo="RJ001",
    defaults={"descricao": "Rio de Janeiro - Copacabana", "usuario": user_rj001},
)
loja_rj.consultores.add(consultor2, consultor3)

loja_mg, created = Loja.objects.get_or_create(
    codigo="MG001",
    defaults={"descricao": "Belo Horizonte - Centro", "usuario": user_mg001},
)
loja_mg.consultores.add(consultor3, consultor4)

# Criar Packs de Grade
print("Criando Packs de Grade...")

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
    ItemPackGrade.objects.create(pack_grade=pack_adulto, tamanho="PP", quantidade=1)
    ItemPackGrade.objects.create(pack_grade=pack_adulto, tamanho="P", quantidade=2)
    ItemPackGrade.objects.create(pack_grade=pack_adulto, tamanho="M", quantidade=3)
    ItemPackGrade.objects.create(pack_grade=pack_adulto, tamanho="G", quantidade=2)
    ItemPackGrade.objects.create(pack_grade=pack_adulto, tamanho="GG", quantidade=1)

# Pack Infantil
pack_infantil, created = PackGrade.objects.get_or_create(
    grade=grade_infantil, nome="Pack Padrão Infantil"
)

if created:
    ItemPackGrade.objects.create(pack_grade=pack_infantil, tamanho="2", quantidade=1)
    ItemPackGrade.objects.create(pack_grade=pack_infantil, tamanho="4", quantidade=2)
    ItemPackGrade.objects.create(pack_grade=pack_infantil, tamanho="6", quantidade=2)
    ItemPackGrade.objects.create(pack_grade=pack_infantil, tamanho="8", quantidade=1)

# Criar Produtos
print("Criando Produtos...")
produto1, created = Produto.objects.get_or_create(
    codigo="DIS001",
    defaults={
        "descricao": "Camiseta Mickey Mouse",
        "licenca": licenca_disney,
        "grade": grade_juvenil,
        "pack_grade": pack_juvenil,
        "preco_unitario": 29.90,
    },
)

produto2, created = Produto.objects.get_or_create(
    codigo="MAR001",
    defaults={
        "descricao": "Camiseta Homem Aranha",
        "licenca": licenca_marvel,
        "grade": grade_adulto,
        "pack_grade": pack_adulto,
        "preco_unitario": 39.90,
    },
)

produto3, created = Produto.objects.get_or_create(
    codigo="PRI001",
    defaults={
        "descricao": "Vestido Elsa Frozen",
        "licenca": licenca_princesas,
        "grade": grade_infantil,
        "pack_grade": pack_infantil,
        "preco_unitario": 49.90,
    },
)

produto4, created = Produto.objects.get_or_create(
    codigo="DIS002",
    defaults={
        "descricao": "Blusa Minnie Mouse",
        "licenca": licenca_disney,
        "grade": grade_adulto,
        "pack_grade": pack_adulto,
        "preco_unitario": 34.90,
    },
)

# Criar Listas de Distribuição
print("Criando Listas de Distribuição...")

# Janeiro 2025
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
    codigo="JAN2025-RJ001-DIS002",
    defaults={
        "mes": 1,
        "ano": 2025,
        "loja": loja_rj,
        "produto": produto4,
        "quantidade_consultor": 15,
        "quantidade_loja": 8,
    },
)

ListaDistribuicao.objects.get_or_create(
    codigo="JAN2025-MG001-DIS001",
    defaults={
        "mes": 1,
        "ano": 2025,
        "loja": loja_mg,
        "produto": produto1,
        "quantidade_consultor": 6,
        "quantidade_loja": 3,
    },
)

# Fevereiro 2025
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

ListaDistribuicao.objects.get_or_create(
    codigo="FEV2025-RJ001-MAR001",
    defaults={
        "mes": 2,
        "ano": 2025,
        "loja": loja_rj,
        "produto": produto2,
        "quantidade_consultor": 11,
        "quantidade_loja": 5,
    },
)

ListaDistribuicao.objects.get_or_create(
    codigo="FEV2025-MG001-DIS002",
    defaults={
        "mes": 2,
        "ano": 2025,
        "loja": loja_mg,
        "produto": produto4,
        "quantidade_consultor": 9,
        "quantidade_loja": 4,
    },
)

print("✅ Banco de dados populado com sucesso!")
print("\n📋 Dados criados:")
print(f"- {Grade.objects.count()} Grades")
print(f"- {Licenca.objects.count()} Licenças")
print(f"- {Consultor.objects.count()} Consultores")
print(f"- {Loja.objects.count()} Lojas")
print(f"- {PackGrade.objects.count()} Packs de Grade")
print(f"- {ItemPackGrade.objects.count()} Itens de Pack")
print(f"- {Produto.objects.count()} Produtos")
print(f"- {ListaDistribuicao.objects.count()} Listas de Distribuição")

print("\n🔐 Usuários criados:")
print("- admin / [senha definida pelo usuário]")
print("- loja_sp001 / loja123")
print("- loja_rj001 / loja123")
print("- loja_mg001 / loja123")

print("\n🚀 Para testar o sistema:")
print("1. Execute: python manage.py runserver")
print("2. Acesse: http://127.0.0.1:8000/")
print("3. Faça login com um dos usuários acima")
print("4. Para administração: http://127.0.0.1:8000/admin/")
