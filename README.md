# Proyecto ERPNext v15 - Setup Local (Sesión 2)

## Requisitos Previos
- Docker y Docker Compose instalados.
- Puertos `8080` (Frontend) y `9000` (WebSocket) libres.

## 🚀 Pasos de Instalación Rápida

1. **Configurar variables de entorno:**
   ```bash
   cp .env.example .env
   ```

2. **Levantar la Infraestructura Docker:**
   ```bash
   docker compose up -d
   ```

3. **Crear el Sitio Inicial:**
   ```bash
   docker compose exec backend bench new-site erpnext.local --admin-password admin --mariadb-root-password admin --force
   ```

4. **Instalar App ERPNext:**
   ```bash
   docker compose exec backend bench --site erpnext.local install-app erpnext
   ```

5. **Acceso:**
   - URL: `http://localhost:8080`
   - Usuario: Administrator
   - Contraseña: admin
