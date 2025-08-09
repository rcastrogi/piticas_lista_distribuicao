# Use Python oficial
FROM python:3.13.2-slim

# Configurar variáveis de ambiente
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE piticas_distribuicao.settings

# Criar diretório de trabalho
WORKDIR /app

# Copiar requirements e instalar dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código da aplicação
COPY . .

# Coletar arquivos estáticos
RUN python manage.py collectstatic --noinput

# Expor porta
EXPOSE 8000

# Comando para iniciar a aplicação
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "piticas_distribuicao.wsgi:application"]
