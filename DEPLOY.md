# 🚀 Guia Rápido de Deploy - Sistema Piticas

## ⚡ Deploy Mais Rápido (Railway)

### 1. Preparação (5 minutos)
```bash
# 1. Subir para GitHub
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/seu-usuario/piticas-distribuicao.git
git push -u origin main
```

### 2. Deploy Railway (5 minutos)
1. Acesse [railway.app](https://railway.app)
2. Login com GitHub
3. "New Project" → "Deploy from GitHub repo"
4. Selecione seu repositório
5. Adicione variáveis de ambiente:
   - `DEBUG=False`
   - `SECRET_KEY=cole-sua-chave-secreta-aqui`
   - `ALLOWED_HOSTS=*.railway.app`

### 3. Configuração Final (2 minutos)
Após deploy, no Railway CLI ou web console:
```bash
python manage.py migrate
python manage.py collectstatic --noinput
python setup_deploy.py
```

### 4. Pronto! 🎉
- Sua aplicação estará rodando em: `https://seu-app.railway.app`
- Admin: `https://seu-app.railway.app/admin/`
- Login: `admin` / `admin123`

---

## 🐳 Alternativa Docker (Local)

### Deploy Local com Docker
```bash
# Construir e executar
docker-compose up --build

# Acessar: http://localhost:8000
```

---

## 📱 Outras Opções

### Heroku
```bash
heroku create piticas-demo
git push heroku main
heroku run python setup_deploy.py
```

### Render
1. Conectar repositório GitHub
2. Build: `pip install -r requirements.txt`
3. Start: `gunicorn piticas_distribuicao.wsgi:application`

### PythonAnywhere (Gratuito)
1. Upload arquivos
2. Configure Web App
3. Execute `python setup_deploy.py`

---

## 🔧 Troubleshooting

### Erro de Static Files
```bash
python manage.py collectstatic --noinput
```

### Erro de Database
```bash
python manage.py migrate
```

### Resetar Dados
```bash
python setup_deploy.py
```

---

## 📋 Checklist de Deploy

- [ ] Repositório no GitHub
- [ ] Arquivos de deploy (Procfile, requirements.txt, runtime.txt)
- [ ] Variáveis de ambiente configuradas
- [ ] Migrações executadas
- [ ] Static files coletados
- [ ] Dados de exemplo criados
- [ ] Admin funcionando

**Total: ~12 minutos para deploy completo!** ⚡
