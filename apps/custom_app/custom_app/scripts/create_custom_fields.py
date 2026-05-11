import frappe

def run():
    frappe.init(site="erpnext.local")
    frappe.connect()
    
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
    
    frappe.db.commit()
