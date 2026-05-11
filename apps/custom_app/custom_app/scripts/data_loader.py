import frappe
import json
import os

def run():
    file_path = "custom_app/data_migration/maestros.json"
    
    if not os.path.exists(file_path):
        file_path = os.path.join(frappe.get_app_path("custom_app"), "data_migration", "maestros.json")
        if not os.path.exists(file_path):
            print(f"Data file not found at: {file_path}")
            return

    with open(file_path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            print("Invalid JSON format in maestros.json")
            return

    for doctype, entries in data.items():
        load_doctype_data(entries, doctype)

def load_doctype_data(data_list, doctype):
    print(f"\nStarting data load for: {doctype}")
    success_count = 0
    error_count = 0
    skipped_count = 0

    for entry in data_list:
        if doctype == "Item":
            identifier = entry.get("item_code")
        elif doctype == "Customer":
            identifier = entry.get("customer_name")
        elif doctype == "Supplier":
            identifier = entry.get("supplier_name")
        else:
            identifier = entry.get("name") or list(entry.values())[0]
        
        try:
            if not frappe.db.exists(doctype, identifier):
                doc_data = {
                    "doctype": doctype,
                    **entry
                }
                
                if doctype == "Item":
                    if not doc_data.get("item_group"):
                        doc_data["item_group"] = "All Item Groups"
                    if not doc_data.get("stock_uom"):
                        doc_data["stock_uom"] = "Nos"
                
                doc = frappe.get_doc(doc_data)
                doc.insert(ignore_permissions=True)
                success_count += 1
                print(f"  [CREATED] {identifier}")
            else:
                skipped_count += 1
                print(f"  [SKIPPED] {identifier} (already exists)")
        
        except Exception as e:
            error_count += 1
            print(f"  [ERROR] {identifier}: {str(e)}")

    frappe.db.commit()
    print(f"Summary for {doctype}: {success_count} created, {skipped_count} skipped, {error_count} errors")
