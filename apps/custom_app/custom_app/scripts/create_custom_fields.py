import frappe

def run():
    
    # --- MEJORAS UX ITEM ---
    if not frappe.db.exists("Custom Field", {"dt": "Item", "fieldname": "warranty_section"}):
        frappe.get_doc({
            "doctype": "Custom Field",
            "dt": "Item",
            "fieldname": "warranty_section",
            "label": "Garantía y Post-Venta",
            "fieldtype": "Section Break",
            "insert_after": "item_group"
        }).insert()

    if not frappe.db.exists("Custom Field", {"dt": "Item", "fieldname": "custom_warranty_period"}):
        frappe.get_doc({
            "doctype": "Custom Field",
            "dt": "Item",
            "fieldname": "custom_warranty_period",
            "label": "Periodo de Garantía (Meses)",
            "fieldtype": "Int",
            "description": "Indica los meses de cobertura oficial del fabricante.",
            "insert_after": "warranty_section"
        }).insert()
    else:
        frappe.db.set_value("Custom Field", "Item-custom_warranty_period", {
            "description": "Indica los meses de cobertura oficial del fabricante.",
            "label": "Periodo de Garantía (Meses)",
            "insert_after": "warranty_section"
        })

    # --- MEJORAS UX CUSTOMER ---
    if not frappe.db.exists("Custom Field", {"dt": "Customer", "fieldname": "responsables_section"}):
        frappe.get_doc({
            "doctype": "Custom Field",
            "dt": "Customer",
            "fieldname": "responsables_section",
            "label": "Asignación de Responsables FluxCore",
            "fieldtype": "Section Break",
            "insert_after": "customer_type"
        }).insert()

    if not frappe.db.exists("Custom Field", {"dt": "Customer", "fieldname": "col_break_1"}):
        frappe.get_doc({
            "doctype": "Custom Field",
            "dt": "Customer",
            "fieldname": "col_break_1",
            "fieldtype": "Column Break",
            "insert_after": "responsables_section"
        }).insert()

    if not frappe.db.exists("Custom Field", {"dt": "Customer", "fieldname": "custom_account_manager"}):
        frappe.get_doc({
            "doctype": "Custom Field",
            "dt": "Customer",
            "fieldname": "custom_account_manager",
            "label": "Gestor de Cuenta",
            "fieldtype": "Link",
            "options": "User",
            "description": "Personal responsable de la relación comercial.",
            "insert_after": "col_break_1"
        }).insert()
    else:
        frappe.db.set_value("Custom Field", "Customer-custom_account_manager", {
            "description": "Personal responsable de la relación comercial.",
            "label": "Gestor de Cuenta",
            "insert_after": "col_break_1"
        })

    if not frappe.db.exists("Custom Field", {"dt": "Customer", "fieldname": "col_break_2"}):
        frappe.get_doc({
            "doctype": "Custom Field",
            "dt": "Customer",
            "fieldname": "col_break_2",
            "fieldtype": "Column Break",
            "insert_after": "custom_account_manager"
        }).insert()

    if not frappe.db.exists("Custom Field", {"dt": "Customer", "fieldname": "custom_tecnico_responsable"}):
        frappe.get_doc({
            "doctype": "Custom Field",
            "dt": "Customer",
            "fieldname": "custom_tecnico_responsable",
            "label": "Técnico Responsable",
            "fieldtype": "Link",
            "options": "User",
            "description": "Personal responsable del soporte técnico.",
            "insert_after": "col_break_2"
        }).insert()
    else:
        frappe.db.set_value("Custom Field", "Customer-custom_tecnico_responsable", {
            "description": "Personal responsable del soporte técnico.",
            "insert_after": "col_break_2"
        })
    
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
