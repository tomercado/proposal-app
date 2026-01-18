# 🌿 Guía de Ramas - Proposal App

## ✅ Ramas Creadas:

- **`main`** - Rama principal (código estable)
- **`tomas-dev`** - Tu rama de desarrollo (Tomas)
- **`amigo-dev`** - Rama de tu amigo

---

## 🎯 Cómo Trabajar con Ramas

### **Para TI (Tomas):**

#### 1. Cambiarte a tu rama:
```bash
git checkout tomas-dev
```

#### 2. Antes de trabajar, actualiza:
```bash
git pull origin tomas-dev
```

#### 3. Haz tus cambios y guárdalos:
```bash
git add .
git commit -m "Descripción de tus cambios"
git push origin tomas-dev
```

#### 4. Cuando termines una funcionalidad completa, fusiona a main:
```bash
# Ir a main
git checkout main

# Actualizar main
git pull origin main

# Fusionar tus cambios
git merge tomas-dev

# Subir a main
git push origin main

# Volver a tu rama
git checkout tomas-dev
```

---

### **Para TU AMIGO:**

#### 1. Después de clonar, cambiarse a su rama:
```bash
git checkout amigo-dev
```

#### 2. Antes de trabajar, actualizar:
```bash
git pull origin amigo-dev
```

#### 3. Hacer cambios y guardarlos:
```bash
git add .
git commit -m "Descripción de los cambios"
git push origin amigo-dev
```

#### 4. Cuando termine una funcionalidad, fusionar a main:
```bash
# Ir a main
git checkout main

# Actualizar main
git pull origin main

# Fusionar sus cambios
git merge amigo-dev

# Subir a main
git push origin main

# Volver a su rama
git checkout amigo-dev
```

---

## 🔄 Sincronizar Cambios entre Ustedes

### Si tu amigo fusionó algo a `main` y tú quieres esos cambios:

```bash
# 1. Ir a main
git checkout main

# 2. Actualizar main
git pull origin main

# 3. Volver a tu rama
git checkout tomas-dev

# 4. Traer los cambios de main a tu rama
git merge main

# 5. Si hay conflictos, resuélvelos y luego:
git add .
git commit -m "Sincronizado con main"
git push origin tomas-dev
```

---

## 📊 Ver en qué rama estás:

```bash
git branch
```

La rama con `*` es donde estás actualmente.

---

## 🎨 Flujo Visual:

```
main (código estable)
 ├── tomas-dev (tú trabajas aquí)
 └── amigo-dev (tu amigo trabaja aquí)
```

**Cada uno trabaja en su rama → Cuando terminan → Fusionan a main**

---

## 💡 Ventajas de este Sistema:

✅ **No se pisan** - Cada uno trabaja en su rama
✅ **Sin conflictos** - Solo fusionan cuando terminan algo
✅ **Código estable** - `main` siempre tiene código que funciona
✅ **Fácil de revertir** - Si algo sale mal, main está intacto

---

## 🆘 Comandos Útiles:

### Ver todas las ramas:
```bash
git branch -a
```

### Cambiar de rama:
```bash
git checkout nombre-rama
```

### Ver diferencias entre ramas:
```bash
git diff main tomas-dev
```

### Eliminar una rama (cuando ya no la necesites):
```bash
git branch -d nombre-rama
```

---

## 📝 Ejemplo de Flujo Completo:

### **Día 1 - Tomas trabaja en Login:**
```bash
git checkout tomas-dev
git pull origin tomas-dev

# Edita routes/auth.py y templates/auth/login.html

git add .
git commit -m "Implementado sistema de login"
git push origin tomas-dev
```

### **Día 1 - Amigo trabaja en Clientes:**
```bash
git checkout amigo-dev
git pull origin amigo-dev

# Edita routes/clients.py y templates/dashboard/clients.html

git add .
git commit -m "Agregada gestión de clientes"
git push origin amigo-dev
```

### **Día 2 - Tomas fusiona su login a main:**
```bash
git checkout main
git pull origin main
git merge tomas-dev
git push origin main
git checkout tomas-dev
```

### **Día 2 - Amigo sincroniza con los cambios de Tomas:**
```bash
git checkout main
git pull origin main
git checkout amigo-dev
git merge main
git push origin amigo-dev
```

---

## 🎯 Resumen Rápido:

**Tu flujo diario:**
```bash
git checkout tomas-dev          # Ir a tu rama
git pull origin tomas-dev       # Actualizar
# Hacer cambios
git add .                       # Agregar cambios
git commit -m "Mensaje"         # Guardar
git push origin tomas-dev       # Subir
```

**Cuando termines algo importante:**
```bash
git checkout main               # Ir a main
git pull origin main            # Actualizar main
git merge tomas-dev             # Fusionar tu trabajo
git push origin main            # Subir a main
git checkout tomas-dev          # Volver a tu rama
```

---

¡Ahora pueden trabajar sin pisarse! 🚀
