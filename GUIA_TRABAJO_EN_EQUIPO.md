# 🤝 Guía de Trabajo en Equipo con Git

## 🎯 Método 1: Simple (Para Empezar)

### ✅ Regla de Oro:
**SIEMPRE haz `git pull` ANTES de empezar a trabajar**

---

### 📝 Flujo de Trabajo Diario:

#### **Antes de empezar a trabajar:**
```bash
# 1. Actualiza tu código con los cambios de tu amigo
git pull origin main
```

#### **Mientras trabajas:**
- Haz tus cambios en los archivos
- Guarda frecuentemente (Ctrl+S)

#### **Cuando termines una funcionalidad:**
```bash
# 1. Ver qué archivos cambiaste
git status

# 2. Agregar todos los cambios
git add .

# 3. Hacer commit con mensaje descriptivo
git commit -m "Agregué login de usuarios"

# 4. IMPORTANTE: Actualizar antes de subir
git pull origin main

# 5. Subir tus cambios
git push origin main
```

---

## ⚠️ ¿Qué pasa si ambos modifican el mismo archivo?

### Escenario: Conflicto de Merge

Cuando hagas `git pull` y ambos editaron el mismo archivo, Git te dirá:

```
CONFLICT (content): Merge conflict in archivo.py
```

### Solución paso a paso:

1. **Abre el archivo con conflicto** en VS Code
2. **Verás algo así:**
```python
<<<<<<< HEAD
# Tu código
def mi_funcion():
    return "Mi versión"
=======
# Código de tu amigo
def mi_funcion():
    return "Versión de mi amigo"
>>>>>>> origin/main
```

3. **Decide qué código mantener:**
   - Haz clic en "Accept Current Change" (tu versión)
   - O "Accept Incoming Change" (versión de tu amigo)
   - O "Accept Both Changes" (ambas versiones)
   - O edita manualmente para combinar lo mejor de ambos

4. **Guarda el archivo**

5. **Completa el merge:**
```bash
git add .
git commit -m "Resuelto conflicto en archivo.py"
git push origin main
```

---

## 🚀 Método 2: Profesional (Con Ramas)

**Recomendado cuando ya tengan más experiencia**

### Concepto:
- Cada uno trabaja en su propia "rama" (branch)
- Cuando terminas, fusionas (merge) tu rama con la principal
- **Evita conflictos** porque no trabajan directamente en `main`

### Flujo con Ramas:

#### **Tú trabajas en una funcionalidad:**
```bash
# 1. Actualizar main
git checkout main
git pull origin main

# 2. Crear tu rama (ejemplo: agregar-login)
git checkout -b agregar-login

# 3. Hacer tus cambios y commits
git add .
git commit -m "Agregué formulario de login"

# 4. Subir tu rama
git push origin agregar-login
```

#### **Tu amigo trabaja en otra funcionalidad:**
```bash
# 1. Actualizar main
git checkout main
git pull origin main

# 2. Crear su rama (ejemplo: agregar-clientes)
git checkout -b agregar-clientes

# 3. Hacer sus cambios y commits
git add .
git commit -m "Agregué gestión de clientes"

# 4. Subir su rama
git push origin agregar-clientes
```

#### **Fusionar cambios a main:**

**Opción A: Desde GitHub (Recomendado)**
1. Ve a GitHub.com
2. Verás un botón "Compare & pull request"
3. Haz clic y crea el Pull Request
4. Revisa los cambios
5. Haz clic en "Merge pull request"
6. Elimina la rama después de fusionar

**Opción B: Desde la terminal**
```bash
# 1. Volver a main
git checkout main

# 2. Actualizar main
git pull origin main

# 3. Fusionar tu rama
git merge agregar-login

# 4. Subir los cambios
git push origin main

# 5. Eliminar la rama local (opcional)
git branch -d agregar-login
```

---

## 📋 Comandos Útiles

### Ver en qué rama estás:
```bash
git branch
```

### Ver todas las ramas (locales y remotas):
```bash
git branch -a
```

### Cambiar de rama:
```bash
git checkout nombre-de-rama
```

### Ver el historial de commits:
```bash
git log --oneline --graph
```

### Deshacer cambios NO guardados:
```bash
git checkout -- nombre-archivo.py
```

### Ver diferencias antes de hacer commit:
```bash
git diff
```

---

## 💡 Mejores Prácticas

### ✅ HACER:
- **Hacer commits pequeños y frecuentes**
  - ✅ "Agregué validación de email"
  - ✅ "Corregí bug en login"
  
- **Mensajes de commit descriptivos**
  - ✅ "Agregué formulario de registro de clientes"
  - ❌ "cambios"
  - ❌ "fix"

- **Hacer `git pull` ANTES de empezar a trabajar**

- **Comunicarse con tu amigo**
  - "Voy a trabajar en el login"
  - "Ya terminé, puedes hacer pull"

### ❌ EVITAR:
- Trabajar en el mismo archivo al mismo tiempo
- Hacer commits gigantes con muchos cambios
- Olvidar hacer `git pull` antes de trabajar
- Mensajes de commit vagos

---

## 🎯 Recomendación para Ustedes

### **Semana 1-2: Método Simple**
- Usen el flujo básico (pull → cambios → commit → push)
- Comuníquense para no editar los mismos archivos
- Ejemplo:
  - **Tú:** Trabajas en `routes/auth.py` y `templates/auth/`
  - **Tu amigo:** Trabaja en `routes/clients.py` y `templates/dashboard/`

### **Semana 3+: Método con Ramas**
- Cuando ya se sientan cómodos con Git
- Cada funcionalidad nueva = una rama nueva
- Usen Pull Requests en GitHub para revisar el código del otro

---

## 🆘 Comandos de Emergencia

### Si metiste la pata y quieres volver atrás:
```bash
# Ver los últimos commits
git log --oneline

# Volver al commit anterior (sin perder cambios)
git reset --soft HEAD~1

# Volver al commit anterior (PERDIENDO cambios)
git reset --hard HEAD~1
```

### Si quieres descartar TODOS tus cambios locales:
```bash
git reset --hard origin/main
```

---

## 📞 Comunicación es Clave

### Antes de trabajar:
💬 "Voy a trabajar en el sistema de login"

### Después de subir cambios:
💬 "Subí cambios en auth.py, haz pull"

### Si hay conflicto:
💬 "Hay conflicto en proposals.py, ¿cuál versión usamos?"

---

## 🎓 Resumen para Empezar HOY

```bash
# ANTES de trabajar (SIEMPRE)
git pull origin main

# Después de hacer cambios
git add .
git commit -m "Descripción clara de lo que hiciste"
git pull origin main  # Por si tu amigo subió algo
git push origin main

# Repetir este ciclo cada vez que termines algo
```

---

¡Con esto ya pueden trabajar juntos sin problemas! 🚀
