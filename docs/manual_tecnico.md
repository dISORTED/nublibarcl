⚙️ Manual Técnico – Dolibarr ERP en la Nube
📋 Descripción
Este manual está dirigido a administradores técnicos del sistema Dolibarr ERP/CRM ejecutado en la plataforma DoliCloud.
Proporciona instrucciones para la configuración inicial, administración de módulos, gestión de usuarios y mantenimiento general.

🖥️ Introducción y primeros pasos
Dolibarr ERP es una solución open source modular que cubre ventas, compras, inventarios, finanzas, proyectos y CRM.
En DoliCloud, ofrece alta disponibilidad, backups automáticos y actualizaciones sin intervención.

🌐 Acceso al sistema
URL: https://<su-empresa>.dolicloud.com

Usuario administrador: (Definido en instalación)

Contraseña: (Guardar en gestor de contraseñas)

Perfiles y roles:

🛠 Administrador – Control total de módulos, usuarios y configuración global.

📦 Comercial – Gestión de clientes, presupuestos y ventas.

💰 Finanzas – Acceso a caja, bancos e informes contables.

⚙️ Personalizado – Configurable en Configuración → Permisos → Roles.

⚙️ Configuración inicial
🏢 Parámetros de empresa
Ruta: Inicio → Configuración → Empresa/Sociedad

RUT/NIF, nombre, dirección y contacto.

Logo corporativo (.png, .jpg, .svg).

Moneda y decimales.

🌍 Localización y formatos
Ruta: Inicio → Configuración → Localización

País, moneda, zona horaria.

Formato de fecha/hora.

🔢 Series de numeración
Ruta: Configuración → Numeración de documentos

Prefijos y longitud para facturas (FAC-0001), pedidos (PED-0001), presupuestos (PRE-0001).

📄 Plantillas de documentos
Ruta: Configuración → Plantillas

Subir plantillas .odt o .docx.

Asociar a tipo de documento.

👥 Usuarios y grupos
Ruta: Configuración → Usuarios

Crear usuarios, asignar roles y agrupar por área.

🧩 Módulos esenciales
📦 Productos y servicios
Ruta: Productos/Servicios → Nuevo producto

Nombre, código, categoría.

Precio de coste y venta, unidad.

Foto, descripción, atributos.

🏭 Inventario
Ruta: Stock → Control de stock

Existencias por almacén.

Movimientos manuales (+/-).

Alerta de stock mínimo.

🧾 Facturación
Ruta: Facturación → Nueva factura

Seleccionar cliente.

Añadir productos/servicios y descuentos.

Generar PDF y enviar por email.

👤 CRM – Terceros y clientes
Ruta: Contactos → Nuevo tercero

Datos fiscales.

Asociar facturas, pedidos, proyectos.

📊 Informes y reportes
Ruta: Informes → Ventas / Stock

Filtrar por período, cliente o producto.

Exportar a Excel/PDF o programar envío.

🔄 Flujos de trabajo
🛒 Ciclo de ventas
Presupuesto → Pedido de cliente → Albarán → Factura.

Registrar cobro en Caja/Bancos.

📥 Ciclo de compras
Pedido a proveedor.

Recepción en Stock.

Factura de proveedor y pago.

💰 Gestión financiera
🏦 Caja y bancos
Ruta: Banca/Caja → Nueva cuenta bancaria

Movimientos de ingreso/egreso.

Conciliación con extractos.

💳 Gastos y pagos
Ruta: Gastos → Nuevo gasto

Registrar facturas recibidas y anticipos.

Programar pagos.

📚 Contabilidad básica
Ruta: Contabilidad → Plan contable

Definir cuentas.

Balances y libro diario.

🛠️ Configuraciones avanzadas
🧩 Gestión de módulos y permisos
Ruta: Configuración → Módulos

Activar/desactivar módulos.

Ajustar permisos en Permisos → Roles.

🔗 Integraciones y API
API REST: Configuración → API → Generar token.

Mailchimp: Configurar clave.

Shopify: Instalar plugin y configurar webhooks.

✉️ Personalizaciones y notificaciones
Plantillas de correo: Configuración → Correo → Plantillas.

Acciones programadas: Cronjobs.

📂 Casos de uso
CroquetasSur

Objetivo: Control de inventario y ventas.

Módulos: Productos, Stock, Facturación.

Resultado: Stock en tiempo real y reportes semanales.

FábricaTextil

Objetivo: Seguimiento de proyectos.

Módulos: Proyectos, Tareas, Finanzas.

Resultado: Control de tiempos y costes.

Consultora XYZ

Objetivo: Facturación de servicios.

Módulos: Terceros, Facturación, Informes.

Resultado: Rentabilidad por cliente y proyecto.

🛡️ Soporte y mantenimiento
Actualizaciones: Aplicadas automáticamente por DoliCloud mensualmente.

Backups: Diarios, retención de 30 días.

Recursos:

Wiki Dolibarr

Foro Dolibarr

GitHub Dolibarr
