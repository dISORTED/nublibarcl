# Runbook de Operación – Nublibar (DoliCloud)

## 1. Alcance
Operación funcional de Dolibarr en DoliCloud (PaaS): monitoreo básico, respaldos manuales, verificación de módulos, tareas de limpieza y atención de incidentes.

## 2. Salud del servicio
- **Login**: Ingresar con usuario operador. Verificar carga del dashboard.
- **Ping API**: `GET /api/index.php/ping` con `DOLAPIKEY`. Debe responder `pong`.
- **Módulos**: Revisión mensual de módulos habilitados y permisos críticos.

## 3. Backups (manual + evidencia)
1. Exportar base de datos desde UI (si tu plan lo permite) o solicitar snapshot a soporte DoliCloud.
2. Exportar CSV de entidades clave (terceros, productos, facturas) y subir a `backups/YYYY-MM-DD/`.
3. Registrar evidencia en `backups/README.md` (fecha, alcance, verificación de restauración en entorno de pruebas si aplica).

## 4. Limpieza de logs (aplicación/servidor)
- Política: retener 30 días.
- Ubicación típica (varía por plan): logs de módulo de email, hooks externos y jobs.
- Verificar tamaño mensual y purgar entradas >30 días.

## 5. Integraciones
- **Postman**: usar la colección incluida. Mantener variables por ambiente (prod/test).
- **Dashboard**: actualizar CSV y ejecutar `make_dashboard.py` si no usas CI. En CI, el job lo hace en cada push.

## 6. Incidentes comunes
- 401/403 API: revisar `DOLAPIKEY`, permisos y módulos.
- Error en exportación CSV: revisar separador, encoding UTF-8 y encabezados esperados.
- GitHub Pages no despliega: confirmar activación de Pages y que `public/` contenga `index.html`.

## 7. Seguridad
- No exponer `DOLAPIKEY` en el repo. Usar variables de entorno/local env en Postman.
- Revisar usuarios inactivos trimestralmente y rotar API keys.

## 8. Mantenimiento programado
- Revisión mensual de integridad de datos (totales de ingresos vs. contabilidad).
- Revisión trimestral de top productos/clientes para ajustes comerciales.

## 9. Contactos y escalamiento
- Responsable Operación: (nombre, email)
- Soporte DoliCloud: (link/portal)
- Auditoría/Contabilidad: (contacto)