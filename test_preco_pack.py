#!/usr/bin/env python
"""
Script para testar as novas funcionalidades de preço total do pack
"""

import os
import sys

import django

# Configurar Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "piticas_distribuicao.settings")
django.setup()

from distribuicao.models import Produto


def testar_preco_pack():
    """Testa as novas funcionalidades de preço do pack"""
    print("=== TESTE DE PREÇO TOTAL DO PACK ===\n")

    produtos = Produto.objects.select_related(
        "pack_grade", "pack_grade__grade"
    ).prefetch_related("pack_grade__itens")

    if not produtos.exists():
        print("Nenhum produto encontrado. Execute o script populate_data.py primeiro.")
        return

    for produto in produtos[:5]:  # Mostrar apenas os primeiros 5 produtos
        print(f"Produto: {produto.codigo} - {produto.descricao}")
        print(f"Pack de Grade: {produto.pack_grade}")
        print(f"Preço Unitário: R$ {produto.preco_unitario:.2f}")

        # Mostrar detalhes do pack
        print("Itens do Pack:")
        total_quantidade = 0
        for item in produto.pack_grade.itens.all():
            print(f"  - {item.tamanho}: {item.quantidade} unidades")
            total_quantidade += item.quantidade

        print(f"Quantidade Total do Pack: {produto.quantidade_total_pack} unidades")
        print(f"Preço Total do Pack: R$ {produto.preco_total_pack:.2f}")
        print(
            f"Verificação: {total_quantidade} x R$ {produto.preco_unitario:.2f} = R$ {total_quantidade * produto.preco_unitario:.2f}"
        )
        print("-" * 60)


if __name__ == "__main__":
    testar_preco_pack()
