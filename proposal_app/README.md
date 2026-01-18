# Proposal App

Sistema de gestión de propuestas comerciales con generación de PDFs.

## Estructura del Proyecto

```
proposal_app/
│
├── app.py                  # Punto de entrada de la aplicación
├── config.py              # Configuración de la aplicación
├── requirements.txt       # Dependencias del proyecto
│
├── database/              # Capa de base de datos
│   ├── db.py             # Inicialización de SQLAlchemy
│   └── models.py         # Modelos de datos
│
├── routes/               # Rutas de la aplicación
│   ├── auth.py          # Autenticación
│   ├── clients.py       # Gestión de clientes
│   ├── proposals.py     # Gestión de propuestas
│   └── pdf.py           # Generación de PDFs
│
├── templates/           # Plantillas HTML
│   ├── auth/           # Plantillas de autenticación
│   ├── dashboard/      # Plantillas del dashboard
│   └── base.html       # Plantilla base
│
└── static/             # Archivos estáticos
    ├── css/           # Estilos CSS
    └── signatures/    # Firmas digitales
```

## Instalación

1. Instalar dependencias:
```bash
pip install -r requirements.txt
```

2. Ejecutar la aplicación:
```bash
python app.py
```

## Características

- ✅ Autenticación de usuarios
- ✅ Gestión de clientes
- ✅ Creación y edición de propuestas
- ✅ Generación de PDFs
- ✅ Vista previa de propuestas
