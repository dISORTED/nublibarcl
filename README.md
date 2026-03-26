# Nublibar

ERP en la nube para PYMEs chilenas, basado en Dolibarr ERP/CRM y operado sobre DoliCloud.

Este repositorio reúne el sitio web informativo del proyecto, documentación funcional y técnica, utilidades de integración, un dashboard estático de KPIs y flujos de automatización con GitHub Actions.

## Resumen

Nublibar nace como una propuesta para ayudar a pequeñas y medianas empresas a centralizar su operación en una sola plataforma, sin tener que administrar infraestructura compleja. La solución se apoya en Dolibarr para cubrir procesos de facturación, inventario, CRM, proyectos y reportes, mientras este repositorio concentra los artefactos de soporte que acompañan esa operación.

En este proyecto encontrarás:

- Sitio comercial estático en HTML, CSS y JavaScript.
- Documentación de usuario, documentación técnica y runbook operacional.
- Scripts de apoyo para respaldo, limpieza de logs y exportación de ventas.
- Dashboard HTML generado desde CSV con Python, Pandas y Plotly.
- Workflows de GitHub Actions para despliegue y generación de artefactos.

## Objetivos del repositorio

- Presentar la propuesta de valor de Nublibar.
- Centralizar documentación de onboarding, operación y mantenimiento.
- Facilitar tareas repetibles de integración con instancias Dolibarr.
- Publicar un dashboard estático de indicadores en GitHub Pages.

## Alcance

Este repositorio no contiene el código fuente de Dolibarr ni una instancia completa del ERP. En cambio, documenta y complementa una operación basada en:

- Dolibarr ERP/CRM como núcleo funcional.
- DoliCloud como plataforma administrada.
- GitHub Pages para publicar contenido estático.
- Scripts locales para tareas auxiliares de operación e integración.

## Arquitectura general

```text
Usuarios
   |
   +-- Sitio informativo estático (HTML/CSS/JS)
   |
   +-- Instancia Dolibarr en DoliCloud
           |
           +-- API REST de Dolibarr
           +-- Módulos ERP habilitados
           +-- Datos exportados en CSV
                    |
                    +-- Dashboard estático en public/
```

## Stack tecnológico

### Frontend estático

- HTML5
- CSS3
- JavaScript vanilla

### Automatización y utilidades

- Python 3.10+ para generación de dashboard y scripts de exportación
- Pandas y Plotly para visualización de KPIs
- Bash para tareas operacionales simples

### Plataforma y operación

- Dolibarr ERP/CRM
- DoliCloud
- GitHub Actions
- GitHub Pages
- Postman para pruebas de API

## Estructura del proyecto

```text
nublibarcl/
├─ .github/workflows/         # CI/CD y automatizaciones
├─ dashboard/                 # Generador del dashboard estático
├─ docs/                      # Manuales y documentación base
├─ img/                       # Imágenes del sitio
├─ integraciones/             # Scripts auxiliares de operación/API
├─ postman/                   # Colección y guía de uso de Postman
├─ runbook/                   # Procedimientos operacionales
├─ index.html                 # Landing principal
├─ nublibar_menu.css          # Estilos del sitio
├─ nublibar_animations.js     # Interacciones del frontend
├─ pyproject.toml             # Configuración de formato/lint para Python
└─ README.md                  # Este documento
```

## Componentes principales

### 1. Sitio web informativo

La landing principal está construida con archivos estáticos:

- `index.html`
- `nublibar_menu.css`
- `nublibar_animations.js`
- `img/`

El sitio presenta:

- propuesta de valor del ERP
- servicios y funcionalidades
- planes comerciales
- caso de éxito
- formulario de contacto

## 2. Dashboard de KPIs

La carpeta `dashboard/` contiene un generador de dashboard HTML que toma un CSV de ventas y produce un archivo listo para publicar en `public/index.html`.

El script:

- lee un CSV con fechas, montos, clientes, productos y cantidades
- calcula ingresos mensuales, número de facturas y ticket promedio
- construye gráficos de ingresos, ticket, top clientes y top productos
- exporta un HTML estático apto para GitHub Pages

Archivo principal:

- `dashboard/make_dashboard.py`

Archivo de ejemplo:

- `dashboard/sample_data.csv`

## 3. Integraciones y scripts operacionales

La carpeta `integraciones/` reúne ejemplos reutilizables para tareas comunes de operación:

- `backup_dolibarr.sh`: respaldo manual de base de datos y documentos
- `limpiar_logs.sh`: limpieza de logs antiguos
- `exportar_ventas_mensuales.py`: exportación mensual de facturas vía API REST

Estos scripts son plantillas y requieren adaptación antes de usarse en producción, especialmente en credenciales, rutas y nombres de instancia.

## 4. Documentación operativa

La documentación se divide en varias capas:

- `docs/manual_usuario.md`: guía funcional y administrativa de uso
- `docs/manual_tecnico.md`: configuración técnica y administración del entorno
- `runbook/OPERACION.md`: procedimientos operacionales, backups, incidentes y mantenimiento
- `postman/README.md`: guía para probar la API con Postman

## Requisitos

### Para editar o visualizar el sitio

- Navegador moderno
- Editor de texto o IDE

### Para generar el dashboard

- Python 3.10 o superior
- `pip`
- Dependencias:
  - `pandas`
  - `plotly`

### Para usar scripts de integración

- Python 3 para `exportar_ventas_mensuales.py`
- Bash, `mysqldump`, `tar` y utilidades GNU para los scripts `.sh`
- Acceso válido a una instancia Dolibarr/DoliCloud
- API key para llamadas REST cuando corresponda

## Puesta en marcha local

### Sitio web estático

Puedes abrir `index.html` directamente en el navegador o levantar un servidor estático local.

Ejemplo con Python:

```bash
python -m http.server 8000
```

Luego abre:

```text
http://localhost:8000
```

## Generación del dashboard

1. Instala dependencias:

```bash
pip install pandas plotly
```

2. Revisa o reemplaza `dashboard/sample_data.csv` por tu exportación real.

3. Ejecuta:

```bash
python dashboard/make_dashboard.py
```

4. El resultado se generará en:

```text
public/index.html
```

## Formato esperado del CSV del dashboard

El generador espera columnas con esta estructura:

- `date` en formato `YYYY-MM-DD`
- `invoice_total` como número
- `customer`
- `product`
- `qty`

## Uso de la API de Dolibarr

El repositorio incluye ejemplos para consumir la API REST de Dolibarr.

Variables habituales:

- `BASE_URL`: URL base de la instancia
- `DOLAPIKEY`: API key del usuario
- `MONTH_START`
- `MONTH_END`

Endpoint de referencia usado en la documentación y scripts:

```text
/api/index.php/ping
```

Si responde `pong`, la conectividad y autenticación básica están correctas.

## Workflows de GitHub Actions

### Deploy Pages

Archivo:

- `.github/workflows/deploy-pages.yml`

Función:

- instala Python 3.11
- instala `pandas` y `plotly`
- ejecuta `dashboard/make_dashboard.py`
- publica `public/` en GitHub Pages

Se activa en `main` cuando hay cambios en:

- `public/**`
- `dashboard/**`
- `.github/workflows/deploy-pages.yml`

### Build PDFs

Archivo:

- `.github/workflows/build-pdf.yml`

Función:

- genera PDF de `README.md`
- genera PDF de `runbook/OPERACION.md`
- publica ambos como artifacts del workflow

### Lint

Existe un workflow de lint en:

- `.github/workflows/lint.yml`

Actualmente está vacío, por lo que conviene completarlo si se quiere validar Python o revisar consistencia del repositorio en CI.

## Configuración de calidad

`pyproject.toml` define reglas básicas para herramientas Python:

- Black con longitud de línea 100
- Flake8 con longitud de línea 100
- ignores `E203` y `W503`

## Seguridad y buenas prácticas

- No subir credenciales ni API keys al repositorio.
- No dejar valores reales en scripts de ejemplo.
- Usar variables de entorno o configuración local para secretos.
- Rotar API keys y revisar permisos periódicamente.
- Verificar respaldos y, cuando sea posible, su restauración en entorno de prueba.
- Revisar usuarios inactivos y accesos privilegiados de forma regular.

## Flujo operativo sugerido

1. Configurar la instancia Dolibarr en DoliCloud.
2. Habilitar módulos y permisos según el negocio.
3. Validar acceso API con Postman.
4. Exportar datos o generar CSV de ventas.
5. Construir el dashboard estático.
6. Publicar contenidos en GitHub Pages.
7. Mantener respaldos, limpieza y revisiones periódicas siguiendo el runbook.

## Casos de uso documentados

La documentación del proyecto menciona escenarios como:

- control de inventario y ventas
- seguimiento de clientes
- generación de reportes comerciales
- operación básica financiera
- soporte a emprendimientos y PYMEs con baja complejidad técnica

También se incluye un caso de referencia para `CroquetasSur`, enfocado en inventario, ventas y control operativo.

## Limitaciones conocidas

- El ERP base depende de Dolibarr/DoliCloud y no se ejecuta desde este repositorio.
- Los scripts de integración vienen como ejemplo y no deben asumirse listos para producción.
- El sitio es estático; el formulario de contacto no tiene backend integrado en este repo.
- El workflow de lint aún no implementa validaciones.
- El dashboard depende de un CSV con estructura esperada y no consulta la API en tiempo real.

## Roadmap sugerido

- Completar workflow de lint.
- Incorporar manejo de variables de entorno para scripts Python.
- Añadir ejemplos de `.env.example` o archivos de configuración seguros.
- Mejorar la documentación de despliegue del sitio y Pages.
- Conectar el formulario de contacto con un backend o servicio externo.
- Añadir más datasets de ejemplo y validaciones para el dashboard.

## Documentación relacionada

- [Manual de usuario](docs/manual_usuario.md)
- [Manual técnico](docs/manual_tecnico.md)
- [Runbook de operación](runbook/OPERACION.md)
- [Dashboard README](dashboard/README.md)
- [Integraciones](integraciones/readme.md)
- [Postman](postman/README.md)

## Licencia y uso

Este repositorio se presenta como material de proyecto, documentación y soporte operativo. Si vas a reutilizarlo en un entorno real, revisa previamente:

- licencias de Dolibarr y sus módulos
- condiciones del servicio DoliCloud
- políticas internas de seguridad y tratamiento de datos

## Autor

Documentación y estructura inicial del proyecto atribuidas a Sebastián Echeverría, según los metadatos incluidos en los manuales y scripts del repositorio.
