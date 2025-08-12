#!/bin/bash
# ========================================
# Script de Backup Manual para Dolibarr ERP
# Autor: Sebastián Echeverría
# Versión: 1.0 - Agosto 2025
# ========================================

# --------- CONFIGURACIÓN POR DEFECTO ---------
DB_HOST="tuservidor.mysql.dolicloud.com"   # Host de la base de datos
DB_NAME="nombre_base_datos"                 # Nombre de la base de datos
DB_USER="usuario_db"                        # Usuario de la base de datos
DB_PASS="contraseña_db"                     # Contraseña de la base de datos
DOCS_PATH="/var/www/documents"              # Carpeta de documentos Dolibarr
DEST_PATH="./backups"                       # Carpeta destino local
# ---------------------------------------------

# --------- PARÁMETROS ---------
while [[ "$#" -gt 0 ]]; do
    case $1 in
        --db-host) DB_HOST="$2"; shift ;;
        --db-name) DB_NAME="$2"; shift ;;
        --db-user) DB_USER="$2"; shift ;;
        --db-pass) DB_PASS="$2"; shift ;;
        --docs-path) DOCS_PATH="$2"; shift ;;
        --dest-path) DEST_PATH="$2"; shift ;;
        *) echo "Parámetro desconocido: $1"; exit 1 ;;
    esac
    shift
done

# --------- FECHA ---------
FECHA=$(date +%Y%m%d_%H%M%S)

# --------- CREAR CARPETA DESTINO ---------
mkdir -p "$DEST_PATH"

# --------- BACKUP BASE DE DATOS ---------
echo "Realizando backup de base de datos..."
mysqldump -h "$DB_HOST" -u "$DB_USER" -p"$DB_PASS" "$DB_NAME" > "$DEST_PATH/dolibarr_db_$FECHA.sql"
if [[ $? -ne 0 ]]; then
    echo "Error al respaldar la base de datos."
    exit 1
fi
echo "Base de datos respaldada: $DEST_PATH/dolibarr_db_$FECHA.sql"

# --------- BACKUP DOCUMENTOS ---------
if [ -d "$DOCS_PATH" ]; then
    echo "Comprimiendo carpeta de documentos..."
    tar -czf "$DEST_PATH/dolibarr_docs_$FECHA.tar.gz" -C "$DOCS_PATH" .
    echo "Documentos respaldados: $DEST_PATH/dolibarr_docs_$FECHA.tar.gz"
else
    echo "Carpeta de documentos no encontrada: $DOCS_PATH"
fi

# --------- FINAL ---------
echo "Backup completado en: $DEST_PATH"
