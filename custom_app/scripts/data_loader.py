import frappe
import json
import os

def run():
    file_path = "custom_app/scripts/data.json"
    
    if not os.path.exists(file_path):
        frappe.throw(f"Data file not found at: {file_path}")

    with open(file_path, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            frappe.throw("Invalid JSON format in data.json")

    if "customers" in data:
        load_doctype_data(data["customers"], "Customer")

    if "items" in data:
        load_doctype_data(data["items"], "Item")

def load_doctype_data(data_list, doctype):
    print(f"Starting data load for: {doctype}")
    success_count = 0
    error_count = 0

    for entry in data_list:
        identifier = entry.get("item_code") if doctype == "Item" else entry.get("customer_name")
        
        try:
            if not frappe.db.exists(doctype, identifier):
                entry.update({"docstatus": 0})
                
                if doctype == "Item":
                    entry.update({"name": entry.get("item_code")})
                    if entry.get("is_stock_item") == 1 and not entry.get("valuation_method"):
                        entry.update({"valuation_method": "FIFO"})

                doc = frappe.get_doc({
                    "doctype": doctype,
                    **entry
                })
                doc.insert(ignore_permissions=True)
                success_count += 1
                print(f"Created: {identifier}")
            else:
                print(f"Skipped (already exists): {identifier}")
        
        except Exception as e:
            error_count += 1
            print(f"Error in {identifier}: {str(e)}")

    frappe.db.commit()
    print(f"Summary for {doctype}: {success_count} success, {error_count} errors")
