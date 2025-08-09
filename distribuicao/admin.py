from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import (
    Consultor,
    Grade,
    ItemPackGrade,
    Licenca,
    ListaDistribuicao,
    Loja,
    PackGrade,
    Produto,
)


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ["codigo", "descricao"]
    search_fields = ["codigo", "descricao"]
    ordering = ["codigo"]


@admin.register(Licenca)
class LicencaAdmin(admin.ModelAdmin):
    list_display = ["codigo", "descricao"]
    search_fields = ["codigo", "descricao"]
    ordering = ["codigo"]


@admin.register(Consultor)
class ConsultorAdmin(admin.ModelAdmin):
    list_display = ["codigo", "nome", "ativo"]
    list_filter = ["ativo"]
    search_fields = ["codigo", "nome"]
    ordering = ["nome"]


class ItemPackGradeInline(admin.TabularInline):
    model = ItemPackGrade
    extra = 1
    min_num = 1


@admin.register(PackGrade)
class PackGradeAdmin(admin.ModelAdmin):
    list_display = ["grade", "nome"]
    list_filter = ["grade"]
    search_fields = ["nome", "grade__codigo", "grade__descricao"]
    ordering = ["grade", "nome"]
    inlines = [ItemPackGradeInline]


@admin.register(Loja)
class LojaAdmin(admin.ModelAdmin):
    list_display = ["codigo", "descricao", "usuario", "ativa"]
    list_filter = ["ativa"]
    search_fields = ["codigo", "descricao"]
    filter_horizontal = ["consultores"]
    ordering = ["codigo"]


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = [
        "codigo",
        "descricao",
        "licenca",
        "get_grade",
        "pack_grade",
        "preco_unitario",
        "get_quantidade_total_pack",
        "get_preco_total_pack",
        "ativo",
    ]
    list_filter = ["licenca", "pack_grade__grade", "ativo"]
    search_fields = ["codigo", "descricao"]
    ordering = ["codigo"]
    fields = [
        "codigo",
        "descricao",
        "licenca",
        "imagem",
        "pack_grade",
        "preco_unitario",
        "ativo",
    ]

    def get_grade(self, obj):
        """Mostra a grade baseada no pack_grade"""
        return obj.grade if obj.grade else "-"

    get_grade.short_description = "Grade"

    def get_quantidade_total_pack(self, obj):
        """Mostra a quantidade total de itens no pack"""
        return obj.quantidade_total_pack

    get_quantidade_total_pack.short_description = "Qtd Pack"

    def get_preco_total_pack(self, obj):
        """Mostra o preço total do pack"""
        return f"R$ {obj.preco_total_pack:.2f}"

    get_preco_total_pack.short_description = "Preço Total Pack"

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "pack_grade":
            # Personalizar a exibição do pack_grade para mostrar a grade
            kwargs["queryset"] = PackGrade.objects.select_related("grade").order_by(
                "grade__codigo", "nome"
            )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(ListaDistribuicao)
class ListaDistribuicaoAdmin(admin.ModelAdmin):
    list_display = [
        "codigo",
        "get_mes_ano",
        "loja",
        "produto",
        "quantidade_consultor",
        "quantidade_loja",
        "quantidade_total",
        "valor_total",
    ]
    list_filter = ["mes", "ano", "loja", "produto__licenca"]
    search_fields = [
        "codigo",
        "loja__codigo",
        "loja__descricao",
        "produto__codigo",
        "produto__descricao",
    ]
    ordering = ["-ano", "-mes", "loja__codigo", "produto__codigo"]
    readonly_fields = ["data_criacao", "data_atualizacao"]

    def get_mes_ano(self, obj):
        mes_nome = dict(ListaDistribuicao.MESES_CHOICES)[obj.mes]
        return f"{mes_nome}/{obj.ano}"

    get_mes_ano.short_description = "Mês/Ano"

    def quantidade_total(self, obj):
        return obj.quantidade_total

    quantidade_total.short_description = "Qtd Total"

    def valor_total(self, obj):
        return f"R$ {obj.valor_total:.2f}"

    valor_total.short_description = "Valor Total"


# Customizar o admin do User para incluir informações da loja
class LojaInline(admin.StackedInline):
    model = Loja
    can_delete = False
    verbose_name_plural = "Loja"
    fields = ["codigo", "descricao", "consultores", "ativa"]
    filter_horizontal = ["consultores"]


class UserAdmin(BaseUserAdmin):
    inlines = (LojaInline,)


# Re-registrar UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Personalizar títulos da administração
admin.site.site_header = "Manutenção Cadastral Piticas"
admin.site.site_title = "Piticas Admin"
admin.site.index_title = "Bem-vindo à Manutenção Cadastral"
