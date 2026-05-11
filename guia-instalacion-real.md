# 🏗️ Manual de Despliegue Técnico: FluxCore Systems (ERPNext v15)

Este documento detalla el procedimiento de instalación, configuración y resolución de incidencias críticas del entorno ERPNext v15 sobre una arquitectura de contenedores Docker en sistemas Windows (WSL2).

---

## 1. 📋 Requisitos del Sistema
Para asegurar la estabilidad del entorno, se requiere:
*   **Docker Desktop**: Versión 4.20 o superior.
*   **Subsistema de Windows para Linux (WSL2)**: Kernel actualizado y distribución base (preferiblemente Ubuntu).
*   **Control de Versiones**: Acceso al repositorio Git del proyecto.

---

## 2. 🚀 Procedimiento de Instalación Estándar

1.  **Inicialización de Variables**: Clonar el archivo de configuración de entorno `.env.example` como `.env` y definir las credenciales de administración.
2.  **Despliegue de Infraestructura**:
    ```bash
    docker compose up -d
    ```
3.  **Verificación de Servicios**: Validar mediante `docker compose ps` que todos los servicios (db, backend, frontend, redis) se encuentren en estado *Running* o *Healthy*.

---

## 🛡️ 3. Registro de Incidencias Críticas y Soluciones Técnicas

Durante el proceso de despliegue, se identificaron y resolvieron los siguientes bloqueos técnicos:

### 3.1. Restricciones de Descarga de Imágenes (ISP Blocking)
*   **Descripción**: Bloqueo sistemático de peticiones hacia Docker Hub por parte del proveedor de servicios de internet.
*   **Resolución**: Implementación de espejos oficiales de **Amazon ECR Public** en el archivo `docker-compose.yml` para asegurar la disponibilidad de las imágenes críticas de base de datos y caché.
    *   *MariaDB Mirror*: `public.ecr.aws/docker/library/mariadb:10.6`
    *   *Redis Mirror*: `public.ecr.aws/docker/library/redis:6.2-alpine`

### 3.2. Fragmentación de Paquetes y Conectividad Externa
*   **Descripción**: Fallos de conectividad (Timeouts) en servicios de resolución de nombres y descarga de dependencias (`pip`, `bench`).
*   **Resolución**: 
    1.  Inyección de DNS públicos de Google (`8.8.8.8`) a nivel de capa de servicio en Docker.
    2.  Ajuste del **MTU (Maximum Transmission Unit)** de la interfaz de red de WSL2 a **1350** para mitigar problemas de fragmentación en redes NAT.

### 3.3. Errores de Pasarela (502 Bad Gateway)
*   **Descripción**: Pérdida de comunicación entre el proxy inverso (Nginx) y el servidor de aplicaciones (Gunicorn) tras cambios en la topología de red.
*   **Resolución**: Ejecución de un ciclo de reinicio completo de la red virtual de Docker (`docker compose down && docker compose up -d`) y depuración de caché mediante `bench clear-cache`.

### 3.4. Restricciones de Autenticación MariaDB (Error 1045)
*   **Descripción**: Fallo en la conexión a la base de datos debido a restricciones de host en el usuario del sitio.
*   **Resolución**: Sincronización manual de privilegios mediante comandos SQL para permitir el acceso desde cualquier host interno del clúster:
    ```sql
    GRANT ALL PRIVILEGES ON `_db_name`.* TO 'db_user'@'%' IDENTIFIED BY 'db_password';
    FLUSH PRIVILEGES;
    ```

### 3.5. Persistencia de Aplicaciones Personalizadas
*   **Descripción**: Volatilidad de las instalaciones de Python en el entorno `custom_app` tras reinicios del contenedor.
*   **Resolución**: Reestructuración del volumen de la aplicación vinculando el directorio local directamente al directorio `/apps` de la instancia de Frappe y configuración del montaje en modo editable (`pip install -e`).

---

## 📂 4. Arquitectura de la Aplicación Personalizada
La lógica de negocio reside en `./custom_app`.
*   **Configuración de Hooks**: El archivo `hooks.py` debe integrar obligatoriamente los metadatos `app_title` y `app_version` para asegurar la compatibilidad con el módulo de información del sistema.
*   **Automatización de Datos**: Los procesos de migración se ejecutan a través de scripts en `custom_app/custom_app/scripts/` invocados mediante el comando `bench execute`.
