# Sistema de Lista de Distribuição - Piticas

Este é um sistema Django completo para gerenciamento de listas de distribuição de produtos com as seguintes funcionalidades:

## 🚀 Funcionalidades Implementadas

### 📋 Cadastros Básicos
- **Grades**: Códigos e descrições (Juvenil, Adulto, Infantil)
- **Licenças**: Códigos e descrições (Disney, Marvel, Princesas)
- **Consultores**: Códigos e nomes
- **Lojas**: Códigos alfanuméricos, descrições e consultores associados

### 👕 Gestão de Produtos
- **Produtos**: Código, descrição, licença, imagem e pack de grade
- **Pack de Grades**: Composição por tamanho e quantidade
  - Exemplo: Grade Juvenil com tamanhos 10(1x), 12(2x), 14(2x), 16(1x)
- **Grade automática**: A grade é definida automaticamente pelo pack selecionado
- **Preços unitários** para cada produto

### 📊 Lista de Distribuição
- **Cadastro por mês e loja** com:
  - Código único
  - Produto
  - Quantidade para consultor
  - Quantidade para loja
  - Cálculos automáticos de totais e valores

### 🔐 Sistema de Segurança
- **Autenticação por loja**: Cada loja tem seu usuário específico
- **Visualização restrita**: Lojas veem apenas suas próprias listas
- **Administradores**: Acesso completo via Manutenção Cadastral

### 📈 Relatórios e Dashboards
- **Dashboard**: Resumo geral com estatísticas
- **Lista filtrada**: Por mês, ano, loja, produto
- **Detalhes da distribuição**: Breakdown completo por tamanho
- **Relatório mensal**: Consolidado por produto e loja

## 🛠️ Tecnologias Utilizadas

- **Backend**: Django 5.2.5
- **Frontend**: Bootstrap 5 + Bootstrap Icons
- **Forms**: django-crispy-forms com Bootstrap 5
- **Upload de imagens**: Pillow
- **Banco de dados**: SQLite (desenvolvimento)

## 📦 Instalação e Configuração

### 1. Configurar o ambiente virtual
```bash
# Instalar dependências
pip install -r requirements.txt
```

### 2. Configurar o banco de dados
```bash
# Aplicar migrações
python manage.py migrate

# Criar superusuário (admin)
python manage.py createsuperuser
```

### 3. Popular com dados de exemplo
```bash
# Executar script de população
python setup_data.py
```

### 4. Executar o servidor
```bash
python manage.py runserver
```

## 🔑 Usuários de Teste

Após executar o script de dados, os seguintes usuários estarão disponíveis:

### Administrador
- **Usuário**: `admin`
- **Senha**: `admin123`
- **Acesso**: Completo a todas as funcionalidades

### Lojas
- **Usuário**: `loja_sp001` | **Senha**: `loja123`
  - Loja: São Paulo - Centro
  - Consultores: Ana Silva, Carlos Santos

- **Usuário**: `loja_rj001` | **Senha**: `loja123`
  - Loja: Rio de Janeiro - Copacabana  
  - Consultores: Carlos Santos, Maria Oliveira

## 🌐 URLs do Sistema

- **Login**: http://127.0.0.1:8000/login/
- **Dashboard**: http://127.0.0.1:8000/
- **Listas de Distribuição**: http://127.0.0.1:8000/listas/
- **Relatório Mensal**: http://127.0.0.1:8000/relatorio/
- **Manutenção Cadastral**: http://127.0.0.1:8000/admin/

## 📋 Estrutura de Dados de Exemplo

### Grades Criadas
- **JUV** - Grade Juvenil (tamanhos: 10, 12, 14, 16)
- **ADT** - Grade Adulto (tamanhos: P, M, G, GG)
- **INF** - Grade Infantil (tamanhos: 2, 4, 6, 8)

### Licenças Criadas
- **DIS** - Disney
- **MAR** - Marvel  
- **PRI** - Princesas Disney

### Produtos de Exemplo
- **DIS001** - Camiseta Mickey Mouse (R$ 29,90)
- **MAR001** - Camiseta Homem Aranha (R$ 39,90)
- **PRI001** - Vestido Elsa Frozen (R$ 49,90)

### Listas de Distribuição
- Criadas para Janeiro e Fevereiro de 2025
- Distribuídas entre as lojas SP001 e RJ001
- Com quantidades variadas para consultores e lojas

## 🎯 Como Usar o Sistema

### Para Lojas
1. Faça login com suas credenciais
2. Visualize suas listas de distribuição no dashboard
3. Use filtros para encontrar listas específicas
4. Visualize detalhes de cada distribuição
5. Gere relatórios mensais

### Para Administradores
1. Acesse a Manutenção Cadastral para gerenciar dados
2. Crie novas grades, licenças, produtos
3. Configure packs de grade com suas composições
4. Cadastre novas lojas e consultores
5. Crie listas de distribuição
6. Visualize relatórios consolidados

## 🔧 Configurações Avançadas

### Personalização da Manutenção Cadastral
A interface de administração foi customizada para incluir:
- Filtros por licença, grade, loja
- Busca por códigos e descrições
- Inlines para edição de packs de grade
- Campos calculados para totais e valores

### Sistema de Permissões
- Lojas veem apenas suas próprias distribuições
- Administradores têm acesso completo
- Validações para garantir integridade dos dados

### Templates Responsivos
- Design adaptável para desktop e mobile
- Navegação intuitiva com sidebar
- Alertas e mensagens de feedback
- Tabelas responsivas com paginação

## 📱 Funcionalidades Especiais

### Cálculos Automáticos
- Total de unidades por distribuição
- Valor total baseado no preço unitário
- Breakdown por tamanho usando packs de grade

### Filtros Inteligentes
- Por período (mês/ano)
- Por loja (para administradores)
- Por produto e licença

### Relatórios Detalhados
- Consolidação por produto
- Totais por loja
- Valores monetários calculados
- Composição detalhada por tamanho

## 🚀 Próximos Passos

O sistema está completo e pronto para uso. Possíveis melhorias futuras incluem:

- Export para Excel/PDF
- Dashboard com gráficos
- Notificações por email
- API REST para integração
- Sistema de aprovação de listas
- Histórico de alterações

## 📞 Suporte

Para dúvidas sobre o sistema, consulte a documentação do Django ou entre em contato com a equipe de desenvolvimento.

---

## 🚀 Deploy para Demonstração

### Opção 1: Railway (Recomendado - Mais Fácil)

1. **Faça fork/clone do projeto**
2. **Acesse [Railway.app](https://railway.app)** e faça login com GitHub
3. **Click em "New Project" → "Deploy from GitHub repo"**
4. **Selecione este repositório**
5. **Railway detectará automaticamente que é Django**
6. **Configurar variáveis de ambiente:**
   - `DEBUG=False`
   - `SECRET_KEY=sua-chave-secreta-aqui`
   - `ALLOWED_HOSTS=*.railway.app`
7. **Deploy automático será feito**
8. **Após deploy, execute:**
   ```bash
   python manage.py migrate
   python manage.py collectstatic --noinput
   python setup_deploy.py
   ```

### Opção 2: Heroku

1. **Instale Heroku CLI**
2. **Comandos no terminal:**
   ```bash
   heroku login
   heroku create piticas-demo
   git add .
   git commit -m "Deploy setup"
   git push heroku main
   heroku run python setup_deploy.py
   ```

### Opção 3: Render

1. **Acesse [Render.com](https://render.com)**
2. **Connect GitHub repository**
3. **Configurações:**
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn piticas_distribuicao.wsgi:application`
4. **Adicionar variáveis de ambiente**
5. **Deploy automático**

### Opção 4: PythonAnywhere (Gratuito)

1. **Crie conta em [PythonAnywhere](https://pythonanywhere.com)**
2. **Upload dos arquivos**
3. **Configure Web App**
4. **Execute setup_deploy.py**

## 🔑 Credenciais de Demonstração

Após o deploy, use estas credenciais:
- **URL Admin:** `/admin/`
- **Username:** `admin`
- **Password:** `admin123`

---

**By Renato Castrogiovanni** 🚀
