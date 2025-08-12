Manual de Usuario de Dolibarr ERP en Nublibar
Portada
Manual de Usuario
Dolibarr ERP en la Nube
Plataforma: DoliCloud
Versión: 1.0
Elaborado por: Sebastián Echeverría
Fecha: Agosto 2025
________________________________________
Índice
1.	Introducción y primeros pasos

2.	Configuración inicial

3.	Módulos esenciales

4.	Flujos de ventas y compras

5.	Gestión financiera

6.	Configuraciones avanzadas

7.	Apéndice por caso de uso

8.	Soporte y mantenimiento
________________________________________



1. Introducción y primeros pasos
Dolibarr ERP es una solución open source modular que cubre todas las necesidades de gestión de una empresa: ventas, compras, inventarios, finanzas, proyectos y CRM. Ejecutado en DoliCloud, ofrece alta disponibilidad, backups automáticos y actualizaciones sin intervención del usuario.
1.1 Acceso al sistema
●	Abra su navegador y vaya a https://<su-empresa>.dolicloud.com.

●	Ingrese sus credenciales (usuario y contraseña).

●	En caso de olvido, haga clic en “¿Olvidó su contraseña?” y siga los pasos para restablecerla.
1.2 Perfiles y roles de usuario
●	Administrador: controla módulos, usuarios y configuración global.

●	Comercial: gestiona clientes, presupuestos y ventas.

●	Finanzas: accede a caja, bancos e informes contables.

●	Personalizado: puede crear roles a medida en: Configuración > Permisos > Roles.
1.3 Interfaz y navegación básica
1.	Barra superior: pestañas de módulos activos (Inicio, Ventas, Stock, Facturación, etc.).

2.	Menú lateral: subopciones del módulo activo.

3.	Buscador global: búsqueda rápida por referencias, nombres o números.
________________________________________

2. Configuración inicial
Antes de operar, configure datos de su empresa y formatos.
2.1 Parámetros de la empresa
Ruta: Inicio > Configuración > Empresa/Sociedad.
- RUT/NIF, nombre, dirección y contacto.
- Cargue logo corporativo (.png, .jpg o .svg).
- Defina moneda y decimales.
2.2 Idioma, zona horaria y formatos
Ruta: Inicio > Configuración > Localización.
- Elija país, moneda y zona horaria.
- Ajuste formato de fecha (DD-MM-YYYY, etc.) y hora.
2.3 Series de numeración
Ruta: Configuración > Numeración de documentos.
- Configure prefijos y longitud para facturas (FAC-0001), pedidos (PED-0001) y presupuestos (PRE-0001).
2.4 Plantillas de documentos
Ruta: Configuración > Plantillas.
- Importe plantillas .odt o .docx.
- Asocie a tipo de documento (factura, albarán, presupuesto).
2.5 Usuarios y grupos
Ruta: Configuración > Usuarios.
- Cree nuevos usuarios y asignarles rol.
- Organice en grupos (ventas, finanzas, almacén).
________________________________________


3. Módulos esenciales
3.1 Productos y servicios
Ruta: Productos/Servicios > Nuevo producto.
1. Introduzca nombre, código y categoría.
2. Defina precio de coste y venta, unidad de medida.
3. Agregue foto, descripción detallada y atributos.
3.2 Inventario
Ruta: Stock > Control de stock.
- Visualice existencias por almacén.
- Registre movimientos manuales (+/-) indicando motivo.
- Active alerta de stock mínimo para reorden automático.
3.3 Facturación
Ruta: Facturación > Nueva factura.
1. Seleccione cliente o cree uno nuevo.
2. Añada productos/servicios y aplique descuentos.
3. Genere PDF y envíe por email con plantilla.
3.4 Terceros y clientes (CRM)
Ruta: Contactos > Nuevo tercero.
- Cree ficha de cliente o proveedor con datos fiscales.
- Asocie facturas, pedidos y proyectos.
3.5 Informes y reportes
Ruta: Informes > Ventas / Stock.
- Filtre por período, cliente o producto.
- Exporte a Excel/PDF o programe envíos automáticos.
________________________________________



4. Flujos de ventas y compras
4.1 Ciclo completo de ventas
1.	Presupuesto: Ventas > Presupuestos > Nuevo.

2.	Pedido de cliente: transforme presupuesto en pedido.

3.	Albarán: crea albarán para registro de entrega.

4.	Factura: convierta albarán en factura y registre cobro en Caja/Bancos.
4.2 Ciclo completo de compras
1.	Solicitud de proveedor: Compras > Pedidos de proveedor > Nuevo.

2.	Recepción: valide mercancía en Stock > Recepciones.

3.	Factura proveedor: contabilice factura y programe pago.
________________________________________5. Gestión financiera
5.1 Caja y bancos
Ruta: Banca/Caja > Nueva cuenta bancaria.
- Registre movimientos de ingreso/egreso.
- Conciliación: importe extracto y asocie movimientos.
5.2 Gastos y pagos
Ruta: Gastos > Nuevo gasto.
- Documente facturas recibidas, anticipos y gastos varios.
- Ejecución de pagos y vinculación a facturas.
5.3 Contabilidad básica
Ruta: Contabilidad > Plan contable.
- Defina cuentas y organícese por grupos.
- Generación de balances y libro diario.
________________________________________
6. Configuraciones avanzadas
6.1 Gestión de módulos y permisos
Ruta: Configuración > Módulos.
- Active/desactive módulos según necesidad.
- En Permisos > Roles ajuste accesos a cada módulo.
6.2 Integraciones y API
●	API REST: habilite en Configuración > API, genere token en perfil.

●	Mailchimp: configure clave en Módulos > Mailchimp.

●	Shopify: instale plugin y configure webhooks en Shopify.
6.3 Personalizaciones y notificaciones
●	Plantillas de correo: Configuración > Correo > Plantillas.

●	Acciones programadas: use Cronjobs para tareas repetitivas.
________________________________________
7. Apéndice por caso de uso
7.1 CroquetasSur
●	Objetivo: mejorar control de inventario y ventas.

●	Módulos usados: Productos, Stock, Facturación.

●	Implementación:
o	Alta de catálogo de productos

o	Configuración de almacén único

o	Flujo ventas → albarán → factura

●	Resultados: stock actualizado en tiempo real, reportes semanales de ventas.


7.2 FábricaTextil
●	Objetivo: seguimiento de proyectos de confección.

●	Módulos usados: Proyectos, Tareas, Finanzas.

●	Resultados: seguimiento de tiempos, control de costes, facturación eficiente.
7.3 Consultora XYZ
●	Objetivo: facturación de servicios profesionales.

●	Módulos usados: Terceros, Facturación, Informes.

●	Resultados: informes de rentabilidad por cliente y proyecto.
________________________________________
8. Soporte y mantenimiento
8.1 Actualizaciones en DoliCloud
DoliCloud aplica parches y actualizaciones sin downtime cada mes.
8.2 Copias de seguridad
Backups automáticos diarios con retención de 30 días.
8.3 Recursos adicionales
●	Wiki Dolibarr: https://wiki.dolibarr.org

●	Foro oficial: https://www.dolibarr.org/forum

●	Código fuente: https://github.com/Dolibarr
________________________________________
Fin del Manual de Usuario 
