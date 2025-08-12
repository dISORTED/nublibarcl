#!/usr/bin/env python3
# ===========================================
# Script: Exportar Ventas Mensuales Dolibarr
# Autor: Sebastián Echeverría
# Versión: 1.0 - Agosto 2025
# ===========================================

import requests
import csv
from datetime import datetime, timedelta

# -------- CONFIGURACIÓN --------
DOLIBARR_URL = "https://<tuempresa>.dolicloud.com/api/index.php"
API_TOKEN = "TOKEN_API_DOLIBARR"  # Generado desde el perfil de usuario en Dolibarr
OUTPUT_FILE = f"ventas_{datetime.now().strftime('%Y_%m')}.csv"

# -------- CALCULAR FECHAS --------
hoy = datetime.now()
inicio_mes = hoy.replace(day=1)
fin_mes = (inicio_mes + timedelta(days=32)).replace(day=1) - timedelta(days=1)

fecha_ini_ts = int(inicio_mes.timestamp())
fecha_fin_ts = int(fin_mes.timestamp())

# -------- CONSULTA API --------
endpoint = f"{DOLIBARR_URL}/invoices"
headers = {
    "DOLAPIKEY": API_TOKEN
}
params = {
    "sortfield": "date",
    "sortorder": "asc",
    "limit": 1000,
    "sqlfilters": f"(t.datef:>=:{fecha_ini_ts}) AND (t.datef:<=:{fecha_fin_ts})"
}

print("Obteniendo facturas del mes actual...")
response = requests.get(endpoint, headers=headers, params=params)

if response.status_code != 200:
    print(f"Error {response.status_code}: {response.text}")
    exit(1)

facturas = response.json()

# -------- GUARDAR CSV --------
with open(OUTPUT_FILE, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Número", "Cliente", "Fecha", "Total (€)"])
    for factura in facturas:
        fecha = datetime.fromtimestamp(factura["date"]).strftime("%Y-%m-%d")
        writer.writerow([factura["ref"], factura["socid"], fecha, factura["total_ttc"]])

print(f"Informe guardado en {OUTPUT_FILE}")
