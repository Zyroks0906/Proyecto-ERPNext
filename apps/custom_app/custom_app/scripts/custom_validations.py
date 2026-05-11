import frappe
from frappe import _

def validate_item_warranty(doc, method):
    """
    Valida que el periodo de garantía sea coherente.
    Sesión 4 - Lógica Funcional (Alejandro)
    """
    if doc.get("custom_warranty_period") is not None:
        if doc.custom_warranty_period < 0:
            frappe.throw(_("El periodo de garantía no puede ser negativo."))
        
        if doc.item_group == "Hardware" and doc.custom_warranty_period == 0:
            frappe.msgprint(_("Advertencia: Los productos de Hardware suelen requerir un periodo de garantía."))

def validate_customer_account_manager(doc, method):
    """
    Asegura que las empresas tengan un gestor de cuenta asignado.
    Sesión 4 - Lógica Funcional (Alejandro)
    """
    if doc.customer_type == "Company" and not doc.get("custom_account_manager"):
        frappe.msgprint(_("Nota: Se recomienda asignar un Gestor de Cuenta para clientes de tipo Empresa."))
