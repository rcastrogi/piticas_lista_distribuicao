# 🆓 Deploy GRATUITO - Sistema Piticas

## 🥇 RENDER.COM (100% Gratuito - RECOMENDADO)

### ✅ Vantagens:
- **Sempre gratuito** para projetos pessoais
- **750 horas/mês** (mais que suficiente)
- **PostgreSQL gratuito** incluído
- **SSL automático**
- **Deploy via GitHub**
- **Não dorme** como Heroku gratuito

### 🚀 Passos para Deploy:

#### 1. Preparar Repositório GitHub (3 min)
```bash
git init
git add .
git commit -m "Deploy para Render"
git branch -M main
git remote add origin https://github.com/seu-usuario/piticas-distribuicao.git
git push -u origin main
```

#### 2. Deploy no Render (5 min)
1. Acesse [render.com](https://render.com) e faça login com GitHub
2. Click em **"New +"** → **"Web Service"**
3. Conecte seu repositório GitHub
4. Configure:
   - **Name**: `piticas-distribuicao`
   - **Branch**: `main`
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate && python setup_deploy.py`
   - **Start Command**: `gunicorn piticas_distribuicao.wsgi:application`

#### 3. Variáveis de Ambiente (2 min)
Adicione no Render:
- `DEBUG` = `False`
- `SECRET_KEY` = `sua-chave-secreta-super-secreta-aqui`
- `ALLOWED_HOSTS` = `*.onrender.com`

#### 4. Pronto! 🎉
- URL: `https://piticas-distribuicao.onrender.com`
- Admin: `https://piticas-distribuicao.onrender.com/admin/`
- Login: `admin` / `admin123`

---

## 🥈 PYTHONANYWHERE (100% Gratuito Permanente)

### ✅ Vantagens:
- **Sempre gratuito**
- **Sem limite de tempo**
- **100MB de espaço**
- **MySQL incluído**

### 🚀 Passos para Deploy:

#### 1. Criar Conta (2 min)
1. Acesse [pythonanywhere.com](https://pythonanywhere.com)
2. Crie conta gratuita

#### 2. Upload do Código (5 min)
1. No dashboard, abra **"Files"**
2. Crie pasta `piticas`
3. Upload todos os arquivos do projeto

#### 3. Configurar Web App (5 min)
1. Vá em **"Web"** → **"Add a new web app"**
2. Escolha **"Manual configuration"**
3. Python 3.10
4. Configure **WSGI file**:
```python
import os
import sys

path = '/home/seuusuario/piticas'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'piticas_distribuicao.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

#### 4. Instalar Dependências (3 min)
No console Bash:
```bash
cd piticas
pip3.10 install --user -r requirements.txt
python3.10 manage.py migrate
python3.10 manage.py collectstatic --noinput
python3.10 setup_deploy.py
```

#### 5. Configurar Static Files
No painel Web:
- **Static files URL**: `/static/`
- **Static files directory**: `/home/seuusuario/piticas/staticfiles/`

---

## 🏅 ALTERNATIVAS EXTRAS

### Fly.io (Gratuito com limites)
- **3 apps gratuitas**
- **Excelente performance**
- **Global deployment**

### Koyeb (Gratuito)
- **Novo provedor**
- **Fácil de usar**
- **Deploy via GitHub**

---

## 📊 Comparação Rápida

| Provedor | Preço | Facilidade | Database | SSL | Uptime |
|----------|-------|------------|----------|-----|---------|
| **Render** | 🆓 | ⭐⭐⭐⭐⭐ | PostgreSQL | ✅ | 99%+ |
| **PythonAnywhere** | 🆓 | ⭐⭐⭐ | MySQL | ✅ | 99%+ |
| Railway | 🆓/💰 | ⭐⭐⭐⭐⭐ | PostgreSQL | ✅ | 99%+ |
| Heroku | 💰 | ⭐⭐⭐⭐ | PostgreSQL | ✅ | 99%+ |

---

## 🎯 RECOMENDAÇÃO FINAL

**Para demonstração rápida**: Use **Render**
- Deploy em 10 minutos
- 100% gratuito
- Funciona perfeitamente

**Para projeto permanente**: Use **PythonAnywhere**
- Gratuito para sempre
- Mais estável a longo prazo

---

## 🔧 Troubleshooting

### Render não faz deploy?
- Verifique se `requirements.txt` está correto
- Build command deve incluir migrations
- Check nos logs do Render

### PythonAnywhere com erro?
- Use Python 3.10 (não 3.13)
- Install com `--user` flag
- Configure WSGI corretamente

**Quer que eu ajude com o deploy específico em alguma dessas plataformas?** 🚀
