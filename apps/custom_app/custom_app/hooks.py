app_name = "custom_app"
app_title = "Custom App"
app_publisher = "Zyroks0906"
app_description = "App personalizada para carga de datos"
app_email = "admin@example.com"
app_license = "mit"

# Esto es lo que falta para que el sistema no falle en el About
app_version = "0.0.1"

# Lógica Funcional - Sesión 4 (Alejandro)
doc_events = {
    "Item": {
        "validate": "custom_app.scripts.custom_validations.validate_item_warranty"
    },
    "Customer": {
        "validate": "custom_app.scripts.custom_validations.validate_customer_account_manager"
    }
}

doctype_js = {
    "Item": "public/js/item.js"
}
