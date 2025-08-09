# ⚡ Deploy no Vercel - Ultrarrápido

## ✅ **Por que Vercel:**
- ✅ **Completamente gratuito**
- ✅ **Deploy automático via GitHub**
- ✅ **CDN global**
- ✅ **Sem configuração**

---

## 🚀 **PASSO A PASSO:**

### **1. Preparar para Vercel**
Criar `vercel.json`:
```json
{
  "version": 2,
  "builds": [
    {
      "src": "piticas_distribuicao/wsgi.py",
      "use": "@vercel/python",
      "config": { "maxLambdaSize": "15mb", "runtime": "python3.9" }
    },
    {
      "src": "build_files.sh",
      "use": "@vercel/static-build",
      "config": {
        "distDir": "staticfiles_build"
      }
    }
  ],
  "routes": [
    {
      "src": "/static/(.*)",
      "dest": "/static/$1"
    },
    {
      "src": "/(.*)",
      "dest": "piticas_distribuicao/wsgi.py"
    }
  ]
}
```

### **2. Criar build script**
`build_files.sh`:
```bash
pip install -r requirements.txt
python manage.py collectstatic --noinput --clear
```

### **3. Deploy**
1. Push para GitHub
2. Conectar no [vercel.com](https://vercel.com)
3. Deploy automático!

**URL**: `https://piticas-distribuicao.vercel.app`
