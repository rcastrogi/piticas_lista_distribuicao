import os
import sys

import django

# Configurar Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "piticas_distribuicao.settings")
django.setup()

from distribuicao.models import Produto

print("=== TESTE DE PREÇO TOTAL DO PACK ===")
produtos = Produto.objects.all()[:3]

for produto in produtos:
    print(f"\nProduto: {produto.codigo} - {produto.descricao}")
    print(f"Preço Unitário: R$ {produto.preco_unitario:.2f}")
    print(f"Quantidade Total do Pack: {produto.quantidade_total_pack}")
    print(f"Preço Total do Pack: R$ {produto.preco_total_pack:.2f}")
