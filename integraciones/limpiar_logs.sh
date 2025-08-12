#!/bin/bash
# ===========================================
# Script: Limpieza de logs antiguos
# Autor: Sebastián Echeverría
# Versión: 1.0 - Agosto 2025
# ===========================================

LOG_PATH="/var/log/dolibarr"  # Cambia a la ruta de tus logs
DIAS=30

echo "Eliminando logs con más de $DIAS días en $LOG_PATH..."
find "$LOG_PATH" -type f -name "*.log" -mtime +$DIAS -exec rm -f {} \;

echo "Limpieza completada."
