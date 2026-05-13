import frappe

def run():
    
    if not frappe.db.exists("Custom Field", {"dt": "Item", "fieldname": "custom_warranty_period"}):
        frappe.get_doc({
            "doctype": "Custom Field",
            "dt": "Item",
            "fieldname": "custom_warranty_period",
            "label": "Warranty Period (Months)",
            "fieldtype": "Int",
            "insert_after": "item_group"
        }).insert()
        print("Custom Field 'custom_warranty_period' created on Item.")
    
    if not frappe.db.exists("Custom Field", {"dt": "Customer", "fieldname": "custom_account_manager"}):
        frappe.get_doc({
            "doctype": "Custom Field",
            "dt": "Customer",
            "fieldname": "custom_account_manager",
            "label": "Account Manager",
            "fieldtype": "Link",
            "options": "User",
            "insert_after": "customer_type"
        }).insert()
        print("Custom Field 'custom_account_manager' created on Customer.")
    
    if not frappe.db.exists("Custom Field", {"dt": "Customer", "fieldname": "custom_tecnico_responsable"}):
        frappe.get_doc({
            "doctype": "Custom Field",
            "dt": "Customer",
            "fieldname": "custom_tecnico_responsable",
            "label": "Técnico Responsable",
            "fieldtype": "Link",
            "options": "User",
            "insert_after": "customer_name"
        }).insert()
        print("Custom Field 'custom_tecnico_responsable' created on Customer.")
    
    # Eliminar campo con acento si existe (limpieza)
    if frappe.db.exists("Custom Field", {"dt": "Customer", "fieldname": "custom_técnico_responsable"}):
        frappe.db.delete("Custom Field", {"dt": "Customer", "fieldname": "custom_técnico_responsable"})
        print("Obsolete accented field 'custom_técnico_responsable' removed.")
    if not frappe.db.exists("Report", "Reporte de Garantías FluxCore"):
        frappe.get_doc({
            "doctype": "Report",
            "report_name": "Reporte de Garantías FluxCore",
            "ref_doctype": "Item",
            "report_type": "Report Builder",
            "json": '{"columns": [["item_code", "Item"], ["item_name", "Item"], ["item_group", "Item"], ["custom_warranty_period", "Item"]]}'
        }).insert()
        print("Report 'Reporte de Garantías FluxCore' created.")
    
    frappe.db.commit()
