import calendar

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import F, Sum
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import FiltroListaForm, LoginForm
from .models import ItemPackGrade, ListaDistribuicao, PackGrade


def login_view(request):
    """View de login personalizada"""
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("dashboard")
            else:
                messages.error(request, "Usuário ou senha inválidos.")
    else:
        form = LoginForm()

    return render(request, "registration/login.html", {"form": form})


@login_required
def dashboard(request):
    """Dashboard principal - mostra resumo das listas de distribuição"""
    # Verificar se o usuário tem uma loja associada
    try:
        loja_usuario = request.user.loja
    except AttributeError:
        loja_usuario = None

    # Se for admin ou superuser, pode ver todas as listas
    if request.user.is_superuser or request.user.is_staff:
        listas = ListaDistribuicao.objects.all()
    elif loja_usuario:
        # Usuário de loja só vê suas próprias listas
        listas = ListaDistribuicao.objects.filter(loja=loja_usuario)
    else:
        listas = ListaDistribuicao.objects.none()
        messages.warning(request, "Seu usuário não está associado a nenhuma loja.")

    # Estatísticas
    total_listas = listas.count()
    valor_total = (
        listas.aggregate(
            total=Sum(
                F("quantidade_consultor")
                + F("quantidade_loja") * F("produto__preco_unitario")
            )
        )["total"]
        or 0
    )

    # Listas recentes
    listas_recentes = listas.order_by("-data_criacao")[:5]

    context = {
        "total_listas": total_listas,
        "valor_total": valor_total,
        "listas_recentes": listas_recentes,
        "loja_usuario": loja_usuario,
    }

    return render(request, "distribuicao/dashboard.html", context)


@login_required
def lista_distribuicao(request):
    """Lista todas as distribuições com filtros"""
    # Verificar permissões
    try:
        loja_usuario = request.user.loja
    except AttributeError:
        loja_usuario = None

    if request.user.is_superuser or request.user.is_staff:
        listas = ListaDistribuicao.objects.select_related(
            "loja", "produto", "produto__licenca"
        )
    elif loja_usuario:
        listas = ListaDistribuicao.objects.filter(loja=loja_usuario).select_related(
            "loja", "produto", "produto__licenca"
        )
    else:
        listas = ListaDistribuicao.objects.none()
        messages.warning(request, "Seu usuário não está associado a nenhuma loja.")

    # Aplicar filtros
    form = FiltroListaForm(request.GET)
    if form.is_valid():
        if form.cleaned_data["mes"]:
            listas = listas.filter(mes=form.cleaned_data["mes"])
        if form.cleaned_data["ano"]:
            listas = listas.filter(ano=form.cleaned_data["ano"])
        if form.cleaned_data["loja"] and (
            request.user.is_superuser or request.user.is_staff
        ):
            listas = listas.filter(loja=form.cleaned_data["loja"])
        if form.cleaned_data["produto"]:
            listas = listas.filter(produto=form.cleaned_data["produto"])

    # Ordenação
    listas = listas.order_by("-ano", "-mes", "loja__codigo", "produto__codigo")

    # Paginação
    paginator = Paginator(listas, 20)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "form": form,
        "loja_usuario": loja_usuario,
    }

    return render(request, "distribuicao/lista_distribuicao.html", context)


@login_required
def detalhe_distribuicao(request, pk):
    """Detalhes de uma distribuição específica"""
    lista = get_object_or_404(ListaDistribuicao, pk=pk)

    # Verificar permissões
    if not (request.user.is_superuser or request.user.is_staff):
        try:
            loja_usuario = request.user.loja
            if lista.loja != loja_usuario:
                messages.error(
                    request, "Você não tem permissão para ver esta distribuição."
                )
                return redirect("lista_distribuicao")
        except AttributeError:
            messages.error(request, "Seu usuário não está associado a nenhuma loja.")
            return redirect("dashboard")

    # Buscar detalhes do pack de grade
    pack_itens = ItemPackGrade.objects.filter(pack_grade=lista.produto.pack_grade)

    context = {
        "lista": lista,
        "pack_itens": pack_itens,
        "mes_nome": calendar.month_name[lista.mes],
    }

    return render(request, "distribuicao/detalhe_distribuicao.html", context)


@login_required
def relatorio_mensal(request):
    """Relatório mensal consolidado"""
    # Verificar permissões
    try:
        loja_usuario = request.user.loja
    except AttributeError:
        loja_usuario = None

    if request.user.is_superuser or request.user.is_staff:
        listas = ListaDistribuicao.objects.all()
    elif loja_usuario:
        listas = ListaDistribuicao.objects.filter(loja=loja_usuario)
    else:
        listas = ListaDistribuicao.objects.none()

    # Filtros
    mes = request.GET.get("mes")
    ano = request.GET.get("ano")

    if mes:
        listas = listas.filter(mes=int(mes))
    if ano:
        listas = listas.filter(ano=int(ano))

    # Agrupar por produto
    relatorio = {}
    for lista in listas.select_related("produto", "loja"):
        produto_key = f"{lista.produto.codigo} - {lista.produto.descricao}"
        if produto_key not in relatorio:
            relatorio[produto_key] = {
                "produto": lista.produto,
                "total_consultor": 0,
                "total_loja": 0,
                "valor_total": 0,
                "lojas": [],
            }

        relatorio[produto_key]["total_consultor"] += lista.quantidade_consultor
        relatorio[produto_key]["total_loja"] += lista.quantidade_loja
        relatorio[produto_key]["valor_total"] += lista.valor_total
        relatorio[produto_key]["lojas"].append(
            {
                "loja": lista.loja,
                "qtd_consultor": lista.quantidade_consultor,
                "qtd_loja": lista.quantidade_loja,
                "valor": lista.valor_total,
            }
        )

    context = {
        "relatorio": relatorio,
        "mes": mes,
        "ano": ano,
        "mes_nome": calendar.month_name[int(mes)] if mes else None,
        "loja_usuario": loja_usuario,
    }

    return render(request, "distribuicao/relatorio_mensal.html", context)


@login_required
def api_pack_grade(request):
    """API para buscar packs de grade baseado na grade selecionada"""
    grade_id = request.GET.get("grade_id")
    if grade_id:
        packs = PackGrade.objects.filter(grade_id=grade_id).values("id", "nome")
        return JsonResponse({"packs": list(packs)})
    return JsonResponse({"packs": []})
