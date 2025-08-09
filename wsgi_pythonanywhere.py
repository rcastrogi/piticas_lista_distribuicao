# WSGI file para PythonAnywhere
# Cole este conteúdo no seu WSGI configuration file
# Substitua 'seuusername' pelo seu username do PythonAnywhere

import os
import sys

# Adicionar o caminho do projeto (SUBSTITUA seuusername pelo seu username)
path = "/home/seuusername/piticas-lista-distribuicao"
if path not in sys.path:
    sys.path.insert(0, path)

# Configurar Django settings
os.environ["DJANGO_SETTINGS_MODULE"] = "piticas_distribuicao.settings_pythonanywhere"

# Importar WSGI application
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
