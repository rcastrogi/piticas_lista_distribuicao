# 🐍 GUIA PRÁTICO: Deploy PythonAnywhere

## 📋 **CHECKLIST DE DEPLOY:**

### ✅ **PASSO 1: Criar Conta (3 min)**

1. **Acesse**: [pythonanywhere.com](https://pythonanywhere.com)
2. **Click**: "Pricing & signup"
3. **Escolha**: "Create a Beginner account" (FREE)
4. **Preencha**: Nome, email, senha
5. **Confirme**: Email de verificação

---

### ✅ **PASSO 2: Upload do Projeto (5 min)**

#### **Opção A: Via GitHub (Recomendado)**
```bash
# 1. Na sua máquina, faça push:
git add .
git commit -m "Deploy para PythonAnywhere"
git push origin main

# 2. No PythonAnywhere, abra "Consoles" → "Bash"
# 3. Execute:
git clone https://github.com/SEU-USUARIO/piticas-lista-distribuicao.git
cd piticas-lista-distribuicao
```

#### **Opção B: Upload ZIP**
1. **Compacte** a pasta do projeto em ZIP
2. **Files** → **Upload a file**
3. **Extract** o ZIP

---

### ✅ **PASSO 3: Configurar Web App (5 min)**

1. **Aba "Web"** → **"Add a new web app"**
2. **Domain**: `seuusername.pythonanywhere.com` (gratuito)
3. **Framework**: **"Manual configuration"**
4. **Python version**: **"Python 3.10"**
5. **Click "Next"**

---

### ✅ **PASSO 4: Configurar WSGI (3 min)**

1. **Na seção "Code"**, click no link **WSGI configuration file**
2. **Delete todo conteúdo** e cole:

```python
import os
import sys

# Adicionar o caminho do projeto (SUBSTITUA seuusername)
path = '/home/seuusername/piticas-lista-distribuicao'
if path not in sys.path:
    sys.path.insert(0, path)

# Configurar Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'piticas_distribuicao.settings_pythonanywhere'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

3. **Save** (Ctrl+S)

---

### ✅ **PASSO 5: Instalar Dependências (3 min)**

1. **Abra "Consoles"** → **"Bash"**
2. **Execute um por vez:**

```bash
# Navegar para o projeto
cd piticas-lista-distribuicao

# Instalar dependências (UMA POR VEZ - importante!)
pip3.10 install --user Django==5.2.5
pip3.10 install --user Pillow==10.4.0
pip3.10 install --user django-crispy-forms==2.3
pip3.10 install --user crispy-bootstrap5==2024.2
pip3.10 install --user whitenoise==6.8.2
```

---

### ✅ **PASSO 6: Configurar Banco e Dados (2 min)**

```bash
# Migrar banco
python3.10 manage.py migrate --settings=piticas_distribuicao.settings_pythonanywhere

# Criar superuser e dados
python3.10 setup_pythonanywhere.py

# Coletar static files
python3.10 manage.py collectstatic --noinput --settings=piticas_distribuicao.settings_pythonanywhere
```

---

### ✅ **PASSO 7: Configurar Static Files (2 min)**

1. **Volte para aba "Web"**
2. **Seção "Static files"**:
   - **URL**: `/static/`
   - **Directory**: `/home/seuusername/piticas-lista-distribuicao/staticfiles/`
3. **Click "Save"**

---

### ✅ **PASSO 8: Ativar e Testar (1 min)**

1. **Click no botão "Reload"** (verde, grande)
2. **Aguarde** reload completar
3. **Click** na URL: `https://seuusername.pythonanywhere.com`

---

## 🎯 **RESULTADO ESPERADO:**

✅ **URL Principal**: `https://seuusername.pythonanywhere.com`
✅ **Admin**: `https://seuusername.pythonanywhere.com/admin/`
✅ **Login**: `admin` / `admin123`
✅ **Dados**: Produtos, grades, licenças já criados

---

## 🔧 **TROUBLESHOOTING:**

### ❌ **Erro 502 Bad Gateway?**
```bash
# Verificar logs
tail /var/log/seuusername.pythonanywhere.com.error.log

# Recriar WSGI
# Verificar path no WSGI file
```

### ❌ **Import Error?**
```bash
# Reinstalar dependências
pip3.10 install --user --upgrade Django
```

### ❌ **Static files não carregam?**
```bash
# Recriar static files
python3.10 manage.py collectstatic --clear --noinput
```

---

## 💡 **DICAS IMPORTANTES:**

1. **Sempre use Python 3.10** no PythonAnywhere
2. **Sempre use --user** ao instalar pacotes
3. **Path WSGI** deve ser exato (substitua seuusername)
4. **Reload** após cada mudança importante

---

## 🎉 **PRÓXIMOS PASSOS:**

Após o deploy funcionar:
1. **Teste todas funcionalidades**
2. **Acesse o admin**
3. **Verifique produtos**
4. **Teste filtros**

**TEMPO TOTAL: ~20 minutos** ⏱️
**CUSTO: R$ 0,00** 💰
