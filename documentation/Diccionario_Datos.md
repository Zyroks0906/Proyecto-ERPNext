# 📖 Diccionario de Datos - ERPNext Custom Fields

Este documento mapea los campos personalizados añadidos a la aplicación ERPNext con sus respectivos tipos de datos en la base de datos MariaDB.

## 🛠️ Campos Personalizados (Custom Fields)

| Doctype (Tabla) | Etiqueta (Label) | Nombre del Campo (Fieldname) | Tipo en Frappe | Tipo en MariaDB | Descripción |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Customer** | Técnico Responsable | `custom_tecnico_responsable` | Link (User) | `VARCHAR(140)` | Enlace al usuario técnico encargado del cliente. |
| **Customer** | Account Manager | `custom_account_manager` | Link (User) | `VARCHAR(140)` | Enlace al gestor de cuentas asignado. |
| **Item** | Warranty Period (Months) | `custom_warranty_period` | Int | `INT(11)` | Periodo de garantía en meses. |
| **Address** | Tax Category | `tax_category` | Link | `VARCHAR(140)` | Categoría de impuestos asociada a la dirección. |
| **Address** | Is Your Company Address | `is_your_company_address` | Check | `INT(1)` | Indica si es una dirección propia de la empresa. |
| **Contact** | Is Billing Contact | `is_billing_contact` | Check | `INT(1)` | Indica si el contacto es para facturación. |
| **Print Settings** | Compact Item Print | `compact_item_print` | Check | `INT(1)` | Opción para impresión compacta de ítems. |
| **Print Settings** | Print UOM after Quantity | `print_uom_after_quantity` | Check | `INT(1)` | Imprime la unidad de medida después de la cantidad. |
| **Print Settings** | Print taxes with zero amount | `print_taxes_with_zero_amount` | Check | `INT(1)` | Permite imprimir impuestos aunque el monto sea cero. |

## 📊 Notas Técnicas
- Los campos de tipo **Link** almacenan el nombre (ID) del documento relacionado, que suele ser un `VARCHAR(140)`.
- Los campos de tipo **Check** se almacenan internamente como booleanos representados por un `INT(1)` (0 o 1).
- Los campos de tipo **Int** se mapean a `INT(11)` estándar de MariaDB.
