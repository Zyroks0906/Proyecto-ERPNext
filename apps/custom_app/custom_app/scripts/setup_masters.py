import frappe

def run():
    print("Inyectando datos maestros necesarios (Versión Final)...")
    
    def ensure_root(doctype, field, name):
        if not frappe.db.exists(doctype, name):
            frappe.get_doc({
                "doctype": doctype,
                field: name,
                "is_group": 1
            }).insert(ignore_permissions=True)
            print(f" - Raíz creada: {name}")
        return name

    # 1. Grupos de Productos
    root_ig = ensure_root("Item Group", "item_group_name", "All Item Groups")
    for group in ["Hardware", "Software"]:
        if not frappe.db.exists("Item Group", group):
            frappe.get_doc({
                "doctype": "Item Group",
                "item_group_name": group,
                "is_group": 0,
                "parent_item_group": root_ig
            }).insert(ignore_permissions=True)
            print(f" - Grupo de Producto creado: {group}")

    # 2. Unidades de Medida
    if not frappe.db.exists("UOM", "Nos"):
        frappe.get_doc({"doctype": "UOM", "uom_name": "Nos", "name": "Nos"}).insert(ignore_permissions=True)
        print(" - UOM 'Nos' creada")

    # 3. Grupo de Clientes
    root_cg = ensure_root("Customer Group", "customer_group_name", "All Customer Groups")
    if not frappe.db.exists("Customer Group", "Commercial"):
        frappe.get_doc({
            "doctype": "Customer Group",
            "customer_group_name": "Commercial",
            "is_group": 0,
            "parent_customer_group": root_cg
        }).insert(ignore_permissions=True)
        print(" - Grupo de Clientes 'Commercial' creado")

    # 4. Grupo de Proveedores
    root_sg = ensure_root("Supplier Group", "supplier_group_name", "All Supplier Groups")
    if not frappe.db.exists("Supplier Group", "Distributor"):
        frappe.get_doc({
            "doctype": "Supplier Group",
            "supplier_group_name": "Distributor",
            "is_group": 0,
            "parent_supplier_group": root_sg
        }).insert(ignore_permissions=True)
        print(" - Grupo de Proveedores 'Distributor' creado")

    # 5. Territorio
    root_ter = ensure_root("Territory", "territory_name", "All Territories")
    if not frappe.db.exists("Territory", "Spain"):
        frappe.get_doc({
            "doctype": "Territory",
            "territory_name": "Spain",
            "is_group": 0,
            "parent_territory": root_ter
        }).insert(ignore_permissions=True)
        print(" - Territorio 'Spain' creado")

    frappe.db.commit()
    print("¡Datos maestros inyectados con éxito!")
