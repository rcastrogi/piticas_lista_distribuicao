## 📋 CHECKLIST DE DEPLOY NO RENDER

### ✅ **PREPARAÇÃO (Concluído)**
- [x] Arquivos de deploy criados
- [x] Git inicializado
- [x] Commit inicial feito

### 🔄 **PRÓXIMOS PASSOS**

#### **PASSO 1: GitHub** ⏱️ 5 min
- [ ] Criar repositório no GitHub
- [ ] Conectar repositório local
- [ ] Fazer push do código
- [ ] Verificar se código apareceu no GitHub

#### **PASSO 2: Render Setup** ⏱️ 3 min  
- [ ] Criar conta no Render.com (gratuita)
- [ ] Conectar com GitHub
- [ ] Criar novo Web Service
- [ ] Selecionar repositório `piticas-lista-distribuicao`

#### **PASSO 3: Configuração** ⏱️ 2 min
- [ ] Build Command: `bash build.sh`
- [ ] Start Command: `gunicorn piticas_distribuicao.wsgi:application`
- [ ] Adicionar variáveis de ambiente:
  - [ ] `DEBUG=False`
  - [ ] `SECRET_KEY=sua-chave-secreta`
  - [ ] `ALLOWED_HOSTS=*.onrender.com`
  - [ ] `DJANGO_SETTINGS_MODULE=piticas_distribuicao.settings_production`

#### **PASSO 4: Deploy** ⏱️ 5-10 min
- [ ] Iniciar deploy
- [ ] Aguardar build completar
- [ ] Verificar logs
- [ ] Testar URL gerada

#### **PASSO 5: Teste** ⏱️ 2 min
- [ ] Acessar aplicação
- [ ] Testar admin (/admin/)
- [ ] Login com admin/admin123
- [ ] Verificar dados de exemplo

### 🎯 **RESULTADO ESPERADO**
- [ ] Aplicação rodando em URL pública
- [ ] Admin funcionando
- [ ] Dados populados
- [ ] Deploy automático configurado

---

**TEMPO TOTAL: ~15 minutos** ⚡

**URL FINAL**: `https://piticas-distribuicao.onrender.com` (exemplo)
