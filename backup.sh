if [ -f .env ]; then
    export $(grep -v '^#' .env | xargs)
fi

TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_DIR="./backups"
OUTPUT_FILE="$BACKUP_DIR/backup_final_$TIMESTAMP.sql"

mkdir -p $BACKUP_DIR

echo "🚀 Iniciando backup de la base de datos MariaDB..."


docker exec db mariadb-dump -u root -p$MYSQL_ROOT_PASSWORD --all-databases > $OUTPUT_FILE

if [ $? -eq 0 ]; then
    echo "✅ Backup completado con éxito: $OUTPUT_FILE"
    cp $OUTPUT_FILE ./backup_final_entrega.sql
    echo "📄 Copia de entrega creada: ./backup_final_entrega.sql"
else
    echo "❌ Error al realizar el backup. Asegúrate de que el contenedor 'db' esté corriendo."
    exit 1
fi
