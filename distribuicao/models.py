from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models


class Grade(models.Model):
    codigo = models.CharField(max_length=20, unique=True, verbose_name="Código")
    descricao = models.CharField(max_length=200, verbose_name="Descrição")

    class Meta:
        verbose_name = "Grade"
        verbose_name_plural = "Grades"
        ordering = ["codigo"]

    def __str__(self):
        return f"{self.codigo} - {self.descricao}"


class Licenca(models.Model):
    codigo = models.CharField(max_length=20, unique=True, verbose_name="Código")
    descricao = models.CharField(max_length=200, verbose_name="Descrição")

    class Meta:
        verbose_name = "Licença"
        verbose_name_plural = "Licenças"
        ordering = ["codigo"]

    def __str__(self):
        return f"{self.codigo} - {self.descricao}"


class Consultor(models.Model):
    codigo = models.CharField(max_length=20, unique=True, verbose_name="Código")
    nome = models.CharField(max_length=200, verbose_name="Nome")
    ativo = models.BooleanField(default=True, verbose_name="Ativo")

    class Meta:
        verbose_name = "Consultor"
        verbose_name_plural = "Consultores"
        ordering = ["nome"]

    def __str__(self):
        return f"{self.codigo} - {self.nome}"


class Loja(models.Model):
    codigo = models.CharField(max_length=20, unique=True, verbose_name="Código")
    descricao = models.CharField(max_length=200, verbose_name="Descrição")
    consultores = models.ManyToManyField(
        Consultor, verbose_name="Consultores", blank=True
    )
    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Usuário de Acesso",
    )
    ativa = models.BooleanField(default=True, verbose_name="Ativa")

    class Meta:
        verbose_name = "Loja"
        verbose_name_plural = "Lojas"
        ordering = ["codigo"]

    def __str__(self):
        return f"{self.codigo} - {self.descricao}"


class PackGrade(models.Model):
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, verbose_name="Grade")
    nome = models.CharField(max_length=200, verbose_name="Nome do Pack")

    class Meta:
        verbose_name = "Pack de Grade"
        verbose_name_plural = "Packs de Grade"
        ordering = ["grade", "nome"]

    def __str__(self):
        return f"{self.grade.codigo} - {self.nome}"


class ItemPackGrade(models.Model):
    pack_grade = models.ForeignKey(
        PackGrade,
        on_delete=models.CASCADE,
        related_name="itens",
        verbose_name="Pack de Grade",
    )
    tamanho = models.CharField(max_length=10, verbose_name="Tamanho")
    quantidade = models.PositiveIntegerField(
        verbose_name="Quantidade", validators=[MinValueValidator(1)]
    )

    class Meta:
        verbose_name = "Item do Pack de Grade"
        verbose_name_plural = "Itens do Pack de Grade"
        unique_together = ["pack_grade", "tamanho"]
        ordering = ["pack_grade", "tamanho"]

    def __str__(self):
        return f"{self.pack_grade} - {self.tamanho}: {self.quantidade}"


class Produto(models.Model):
    codigo = models.CharField(max_length=50, unique=True, verbose_name="Código")
    descricao = models.CharField(max_length=200, verbose_name="Descrição")
    licenca = models.ForeignKey(
        Licenca, on_delete=models.CASCADE, verbose_name="Licença"
    )
    imagem = models.ImageField(
        upload_to="produtos/", null=True, blank=True, verbose_name="Imagem"
    )
    pack_grade = models.ForeignKey(
        PackGrade, on_delete=models.CASCADE, verbose_name="Pack de Grade"
    )
    preco_unitario = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Preço Unitário"
    )
    ativo = models.BooleanField(default=True, verbose_name="Ativo")

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ["codigo"]

    def __str__(self):
        return f"{self.codigo} - {self.descricao}"

    @property
    def grade(self):
        """Retorna a grade baseada no pack_grade selecionado"""
        return self.pack_grade.grade if self.pack_grade else None

    @property
    def quantidade_total_pack(self):
        """Retorna a quantidade total de itens no pack"""
        if self.pack_grade:
            return sum(item.quantidade for item in self.pack_grade.itens.all())
        return 0

    @property
    def preco_total_pack(self):
        """Retorna o preço total do pack (quantidade total * preço unitário)"""
        return self.quantidade_total_pack * self.preco_unitario

    def save(self, *args, **kwargs):
        # A grade será determinada automaticamente pelo pack_grade
        super().save(*args, **kwargs)


class ListaDistribuicao(models.Model):
    MESES_CHOICES = [
        (1, "Janeiro"),
        (2, "Fevereiro"),
        (3, "Março"),
        (4, "Abril"),
        (5, "Maio"),
        (6, "Junho"),
        (7, "Julho"),
        (8, "Agosto"),
        (9, "Setembro"),
        (10, "Outubro"),
        (11, "Novembro"),
        (12, "Dezembro"),
    ]

    codigo = models.CharField(max_length=50, unique=True, verbose_name="Código")
    mes = models.IntegerField(choices=MESES_CHOICES, verbose_name="Mês")
    ano = models.IntegerField(verbose_name="Ano")
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE, verbose_name="Loja")
    produto = models.ForeignKey(
        Produto, on_delete=models.CASCADE, verbose_name="Produto"
    )
    quantidade_consultor = models.PositiveIntegerField(
        verbose_name="Quantidade para Consultor", validators=[MinValueValidator(0)]
    )
    quantidade_loja = models.PositiveIntegerField(
        verbose_name="Quantidade para Loja", validators=[MinValueValidator(0)]
    )
    data_criacao = models.DateTimeField(
        auto_now_add=True, verbose_name="Data de Criação"
    )
    data_atualizacao = models.DateTimeField(
        auto_now=True, verbose_name="Data de Atualização"
    )

    class Meta:
        verbose_name = "Lista de Distribuição"
        verbose_name_plural = "Listas de Distribuição"
        unique_together = ["mes", "ano", "loja", "produto"]
        ordering = ["-ano", "-mes", "loja__codigo", "produto__codigo"]

    def __str__(self):
        mes_nome = dict(self.MESES_CHOICES)[self.mes]
        return f"{self.codigo} - {mes_nome}/{self.ano} - {self.loja.codigo} - {self.produto.codigo}"

    @property
    def quantidade_total(self):
        return self.quantidade_consultor + self.quantidade_loja

    @property
    def valor_total(self):
        return self.quantidade_total * self.produto.preco_unitario
