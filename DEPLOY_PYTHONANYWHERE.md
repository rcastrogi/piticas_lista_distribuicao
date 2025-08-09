# 🐍 Deploy no PythonAnywhere - 100% Gratuito

## ✅ **Por que PythonAnywhere é Melhor:**
- ✅ **100% Gratuito para sempre**
- ✅ **Sem problemas de psycopg2**
- ✅ **MySQL incluído (gratuito)**
- ✅ **Interface web simples**
- ✅ **Upload direto de arquivos**

---

## 🚀 **PASSO A PASSO (15 minutos):**

### **1. Criar Conta (2 min)**
1. Acesse [pythonanywhere.com](https://pythonanywhere.com)
2. Click **"Pricing & signup"**
3. **"Create a Beginner account"** (gratuito)
4. Preencha dados e confirme email

### **2. Upload dos Arquivos (5 min)**
1. No dashboard, click **"Files"**
2. Click **"Upload a file"**
3. Faça upload do arquivo ZIP do projeto
4. OU use Git:
   ```bash
   git clone https://github.com/seu-usuario/piticas-lista-distribuicao.git
   ```

### **3. Configurar Web App (5 min)**
1. Aba **"Web"** → **"Add a new web app"**
2. Escolha **"Manual configuration"**
3. **Python 3.10** (recomendado)
4. Click **"Next"**

### **4. Configurar WSGI (3 min)**
1. Na seção **"Code"**, click no link **WSGI configuration file**
2. Substitua todo conteúdo por:
```python
import os
import sys

# Caminho para seu projeto
path = '/home/seuusername/piticas-lista-distribuicao'
if path not in sys.path:
    sys.path.insert(0, path)

# Configurar Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'piticas_distribuicao.settings_pythonanywhere'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

### **5. Instalar Dependências**
1. Abra **"Consoles"** → **"Bash"**
2. Execute:
```bash
cd piticas-lista-distribuicao
pip3.10 install --user Django==5.2.5
pip3.10 install --user Pillow==10.4.0
pip3.10 install --user django-crispy-forms==2.3
pip3.10 install --user crispy-bootstrap5==2024.2
pip3.10 install --user whitenoise==6.8.2
```

### **6. Configurar Banco e Static Files**
```bash
python3.10 manage.py migrate
python3.10 manage.py collectstatic --noinput
python3.10 setup_pythonanywhere.py
```

### **7. Configurar Static Files (Web Tab)**
- **Static files URL**: `/static/`
- **Static files directory**: `/home/seuusername/piticas-lista-distribuicao/staticfiles/`

### **8. Reload e Testar**
1. Click **"Reload"** no Web tab
2. Acesse sua URL: `https://seuusername.pythonanywhere.com`

---

## 🎯 **URL FINAL:**
`https://seuusername.pythonanywhere.com/admin/`
**Login**: admin / admin123

**Funciona 100% sem problemas de psycopg2!** 🎉
