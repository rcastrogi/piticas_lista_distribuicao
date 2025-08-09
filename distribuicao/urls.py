from django.urls import path

from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("login/", views.login_view, name="login"),
    path("listas/", views.lista_distribuicao, name="lista_distribuicao"),
    path("listas/<int:pk>/", views.detalhe_distribuicao, name="detalhe_distribuicao"),
    path("relatorio/", views.relatorio_mensal, name="relatorio_mensal"),
    path("api/pack-grade/", views.api_pack_grade, name="api_pack_grade"),
]
