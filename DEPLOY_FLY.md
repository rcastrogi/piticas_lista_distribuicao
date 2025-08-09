# 🚁 Deploy no Fly.io - Moderno e Gratuito

## ✅ **Por que Fly.io:**
- ✅ **Gratuito até 3 apps**
- ✅ **Deploy via Docker**
- ✅ **Global CDN**
- ✅ **PostgreSQL gratuito**

---

## 🚀 **PASSO A PASSO:**

### **1. Instalar Fly CLI**
```bash
# Windows
powershell -Command "iwr https://fly.io/install.ps1 -useb | iex"

# Ou baixar em: https://fly.io/docs/getting-started/installing-flyctl/
```

### **2. Login e Setup**
```bash
fly auth signup  # ou fly auth login
fly launch
```

### **3. Configurar fly.toml**
```toml
app = "piticas-distribuicao"
primary_region = "gru"  # São Paulo

[build]
  dockerfile = "Dockerfile.dev"

[env]
  DJANGO_SETTINGS_MODULE = "piticas_distribuicao.settings_docker"

[[services]]
  http_checks = []
  internal_port = 8000
  processes = ["app"]
  protocol = "tcp"
  script_checks = []

  [[services.ports]]
    force_https = true
    handlers = ["http"]
    port = 80

  [[services.ports]]
    handlers = ["tls", "http"]
    port = 443
```

### **4. Deploy**
```bash
fly deploy
```

### **5. Configurar Secrets**
```bash
fly secrets set SECRET_KEY="sua-chave-secreta"
fly secrets set DEBUG="False"
fly secrets set ALLOWED_HOSTS="*.fly.dev"
```

**URL Final**: `https://piticas-distribuicao.fly.dev`
