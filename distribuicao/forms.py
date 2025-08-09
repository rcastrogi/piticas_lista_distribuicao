import datetime

from django import forms

from .models import ListaDistribuicao, Loja, PackGrade, Produto


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Nome de usuário"}
        ),
        label="Usuário",
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Senha"}
        ),
        label="Senha",
    )


class FiltroListaForm(forms.Form):
    MESES_CHOICES = [("", "Todos os meses")] + ListaDistribuicao.MESES_CHOICES

    mes = forms.ChoiceField(
        choices=MESES_CHOICES,
        required=False,
        widget=forms.Select(attrs={"class": "form-control"}),
        label="Mês",
    )

    ano = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "min": 2020,
                "max": 2030,
                "value": datetime.datetime.now().year,
            }
        ),
        label="Ano",
    )

    loja = forms.ModelChoiceField(
        queryset=Loja.objects.filter(ativa=True),
        required=False,
        empty_label="Todas as lojas",
        widget=forms.Select(attrs={"class": "form-control"}),
        label="Loja",
    )

    produto = forms.ModelChoiceField(
        queryset=Produto.objects.filter(ativo=True),
        required=False,
        empty_label="Todos os produtos",
        widget=forms.Select(attrs={"class": "form-control"}),
        label="Produto",
    )


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = [
            "codigo",
            "descricao",
            "licenca",
            "imagem",
            "pack_grade",
            "preco_unitario",
        ]
        widgets = {
            "codigo": forms.TextInput(attrs={"class": "form-control"}),
            "descricao": forms.TextInput(attrs={"class": "form-control"}),
            "licenca": forms.Select(attrs={"class": "form-control"}),
            "imagem": forms.FileInput(attrs={"class": "form-control"}),
            "pack_grade": forms.Select(
                attrs={"class": "form-control", "id": "id_pack_grade"}
            ),
            "preco_unitario": forms.NumberInput(
                attrs={"class": "form-control", "step": "0.01"}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ordenar pack_grade por grade para melhor visualização
        self.fields["pack_grade"].queryset = PackGrade.objects.select_related(
            "grade"
        ).order_by("grade__codigo", "nome")

        # Adicionar help text para mostrar que a grade é definida pelo pack
        self.fields[
            "pack_grade"
        ].help_text = (
            "Selecione o pack de grade. A grade será definida automaticamente."
        )


class ListaDistribuicaoForm(forms.ModelForm):
    class Meta:
        model = ListaDistribuicao
        fields = [
            "codigo",
            "mes",
            "ano",
            "loja",
            "produto",
            "quantidade_consultor",
            "quantidade_loja",
        ]
        widgets = {
            "codigo": forms.TextInput(attrs={"class": "form-control"}),
            "mes": forms.Select(attrs={"class": "form-control"}),
            "ano": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": 2020,
                    "max": 2030,
                    "value": datetime.datetime.now().year,
                }
            ),
            "loja": forms.Select(attrs={"class": "form-control"}),
            "produto": forms.Select(attrs={"class": "form-control"}),
            "quantidade_consultor": forms.NumberInput(
                attrs={"class": "form-control", "min": 0}
            ),
            "quantidade_loja": forms.NumberInput(
                attrs={"class": "form-control", "min": 0}
            ),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)

        # Se o usuário não é admin/staff, filtrar apenas sua loja
        if user and not (user.is_superuser or user.is_staff):
            try:
                loja_usuario = user.loja
                self.fields["loja"].queryset = Loja.objects.filter(pk=loja_usuario.pk)
                self.fields["loja"].initial = loja_usuario
            except AttributeError:
                self.fields["loja"].queryset = Loja.objects.none()
        else:
            self.fields["loja"].queryset = Loja.objects.filter(ativa=True)

        self.fields["produto"].queryset = Produto.objects.filter(ativo=True)
