#!/usr/bin/env python3
"""
Genera un dashboard HTML estático con KPIs de Nublibar.
Lee `sample_data.csv` (o un CSV exportado de Dolibarr) con columnas:
 - date (YYYY-MM-DD), invoice_total (float), customer, product, qty
Salida: `public/index.html` listo para GitHub Pages.
"""
import pandas as pd
from pathlib import Path
import plotly.express as px
import plotly.graph_objects as go

DATA_CSV = Path(__file__).parent / "sample_data.csv"
OUT_DIR = Path(__file__).parent.parent / "public"
OUT_FILE = OUT_DIR / "index.html"

OUT_DIR.mkdir(parents=True, exist_ok=True)

# 1) Cargar datos
if not DATA_CSV.exists():
    raise SystemExit(f"No existe {DATA_CSV} – sube tu CSV de ventas.")

df = pd.read_csv(DATA_CSV, parse_dates=["date"])

# 2) KPIs básicos
monthly = df.set_index("date").resample("MS").agg(
    revenue=("invoice_total", "sum"),
    invoices=("invoice_total", "count"),
    qty=("qty", "sum"),
)
monthly["avg_ticket"] = monthly["revenue"] / monthly["invoices"].where(monthly["invoices"]>0, 1)

# Top clientes/productos
top_customers = df.groupby("customer")["invoice_total"].sum().nlargest(10).reset_index()
product_sales = df.groupby("product")["qty"].sum().nlargest(10).reset_index()

# 3) Gráficos
fig_rev = px.line(
    monthly.reset_index(), x="date", y="revenue", title="Ingresos por mes"
)
fig_ticket = px.bar(
    monthly.reset_index(), x="date", y="avg_ticket", title="Ticket promedio por mes"
)
fig_top_cust = px.bar(
    top_customers, x="customer", y="invoice_total", title="Top 10 Clientes por Ingresos"
)
fig_top_prod = px.bar(
    product_sales, x="product", y="qty", title="Top 10 Productos por Cantidad"
)

# 4) KPI cards (como tabla simple)
last = monthly.tail(1)
if not last.empty:
    kpi_html = f"""
    <div class='kpis'>
      <div class='kpi'><h3>Ingresos último mes</h3><p>${last['revenue'].iloc[0]:,.0f}</p></div>
      <div class='kpi'><h3>Facturas último mes</h3><p>{int(last['invoices'].iloc[0])}</p></div>
      <div class='kpi'><h3>Ticket promedio</h3><p>${last['avg_ticket'].iloc[0]:,.0f}</p></div>
    </div>
    """
else:
    kpi_html = "<p>Sin datos para KPIs.</p>"

# 5) Construir HTML único
html = f"""
<!doctype html>
<html lang='es'>
<head>
  <meta charset='utf-8'>
  <meta name='viewport' content='width=device-width, initial-scale=1'>
  <title>Nublibar – Dashboard</title>
  <style>
    body {{ font-family: system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial; margin: 24px; }}
    .wrap {{ max-width: 1100px; margin: 0 auto; }}
    header {{ display:flex; justify-content:space-between; align-items:center; margin-bottom: 16px; }}
    .kpis {{ display:grid; grid-template-columns: repeat(3, 1fr); gap: 12px; margin: 12px 0 24px; }}
    .kpi {{ background:#f5f7fa; border:1px solid #e6e9ef; border-radius:12px; padding:16px; }}
    .chart {{ margin: 20px 0; }}
    footer {{ margin-top: 32px; color:#6b7280; font-size: 13px; }}
    @media(max-width: 768px) {{ .kpis {{ grid-template-columns: 1fr; }} }}
  </style>
</head>
<body>
  <div class='wrap'>
    <header>
      <h1>Nublibar – Dashboard de KPIs</h1>
      <span>{pd.Timestamp.utcnow().strftime('%Y-%m-%d %H:%M UTC')}</span>
    </header>
    {kpi_html}
    <div class='chart'>{fig_rev.to_html(include_plotlyjs='cdn', full_html=False)}</div>
    <div class='chart'>{fig_ticket.to_html(include_plotlyjs='cdn', full_html=False)}</div>
    <div class='chart'>{fig_top_cust.to_html(include_plotlyjs='cdn', full_html=False)}</div>
    <div class='chart'>{fig_top_prod.to_html(include_plotlyjs='cdn', full_html=False)}</div>
    <footer>Generado por <code>dashboard/make_dashboard.py</code>.</footer>
  </div>
</body>
</html>
"""

OUT_FILE.write_text(html, encoding="utf-8")
print(f"Dashboard generado en {OUT_FILE}")