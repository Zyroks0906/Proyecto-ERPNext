#!/bin/bash

if [ -f .env ]; then
    export $(grep -v '^#' .env | xargs)
fi

TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_DIR="./backups"
DB_CONTAINER="db"
DB_NAME=${DB_NAME:-"_1be545f49615560a"}
ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD}

mkdir -p $BACKUP_DIR

echo "🚀 Iniciando dump de la base de datos MariaDB..."

docker exec $DB_CONTAINER /usr/bin/mysqldump -u root -p$ROOT_PASSWORD --all-databases > $BACKUP_DIR/db_backup_$TIMESTAMP.sql

if [ $? -eq 0 ]; then
    echo "✅ Backup completado con éxito: $BACKUP_DIR/db_backup_$TIMESTAMP.sql"
else
    echo "❌ Error al realizar el backup."
    exit 1
fi
