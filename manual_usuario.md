# ⚙️ Manual Usuario – Nublibar ERP (Dolibarr)

## 📋 Descripción
Este manual está dirigido a administradores técnicos del sistema **Nublibar ERP** basado en **Dolibarr ERP/CRM**.  
Proporciona instrucciones para la administración, mantenimiento y configuración avanzada del entorno.

---

## 🖥️ Acceso al sistema
- **URL de acceso**: *(Colocar aquí la URL de tu instancia en DoliCloud)*  
- **Usuario administrador**: *(Definir usuario admin creado en la instalación)*  
- **Contraseña**: *(Mantener en un gestor seguro de contraseñas)*  

---

## 🔑 Gestión de usuarios
1. Iniciar sesión como **Administrador**.
2. Navegar a **Inicio → Configuración → Usuarios y Grupos**.
3. Crear usuarios con los roles correspondientes:
   - **Administrador**: Control total del sistema.
   - **Usuario estándar**: Acceso limitado a módulos asignados.
4. Asignar permisos por módulo según las necesidades.

---

## 🧩 Administración de módulos
1. Ir a **Inicio → Configuración → Módulos**.
2. Activar/desactivar módulos según la operativa de la empresa (Ej: Facturación, Almacén, Proyectos).
3. Configurar parámetros de cada módulo después de activarlo.

---

## 💾 Copias de seguridad
- **Frecuencia recomendada**: Diario o semanal según el uso.
- Desde el panel de DoliCloud:
  1. Acceder a la sección **Backup/Restore**.
  2. Descargar copia de la base de datos y de los documentos.
- Guardar las copias en un almacenamiento seguro (ej. Google Drive con cifrado).

---

## 🔒 Seguridad
- Habilitar **doble autenticación (2FA)** para el usuario administrador si está disponible.
- Cambiar contraseñas periódicamente.
- Limitar el acceso a direcciones IP confiables (si la plataforma lo soporta).

---

## 📈 Monitorización y mantenimiento
- Revisar **logs de sistema** para detectar errores o accesos sospechosos.
- Mantener módulos y extensiones actualizados.
- Revisar espacio de almacenamiento y rendimiento del servidor desde DoliCloud.

---

## 🛠️ Resolución de problemas comunes
| Problema | Posible causa | Solución |
|----------|--------------|----------|
| No puedo iniciar sesión | Contraseña incorrecta o usuario bloqueado | Restablecer contraseña desde cuenta admin |
| Módulo no carga | No está activado o mal configurado | Activar en Configuración → Módulos |
| Lentitud en el sistema | Alta carga o falta de recursos | Revisar uso de recursos y optimizar datos |

---

## 📄 Recursos adicionales
- [Documentación oficial Dolibarr](https://wiki.dolibarr.org/index.php/Main_Page)
- [Foro de soporte Dolibarr](https://www.dolibarr.org/forum/)
- [Portal DoliCloud](https://www.dolicloud.com/)

---

✏ **Nota**: Este manual debe actualizarse cada vez que se hagan cambios significativos en la configuración o se incorporen nuevos módulos.
