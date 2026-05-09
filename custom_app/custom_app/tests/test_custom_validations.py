import frappe
from frappe.tests.utils import FrappeTestCase

class TestCustomValidations(FrappeTestCase):
    """
    Suite de pruebas técnicas para validaciones funcionales de FluxCore Systems.
    Sigue estándares de desarrollo Senior para ERPNext/Frappe.
    """

    def setUp(self):
        """Configuración previa a cada test: Limpieza de datos de prueba."""
        frappe.db.delete("Item", {"item_code": ["like", "TEST-ITEM-%"]})
        frappe.db.delete("Customer", {"customer_name": ["like", "TEST-CUST-%"]})

    def test_item_warranty_negative_validation(self):
        """PRUEBA: Bloqueo de periodos de garantía negativos."""
        item = frappe.get_doc({
            "doctype": "Item",
            "item_code": "TEST-ITEM-NEG",
            "item_name": "Servidor de Prueba",
            "item_group": "Hardware",
            "stock_uom": "Nos",
            "custom_warranty_period": -12
        })
        
        # Debe lanzar ValidationError al intentar validar/guardar
        self.assertRaises(frappe.ValidationError, item.insert)

    def test_item_hardware_warranty_warning(self):
        """PRUEBA: Verificación de lógica de advertencia para Hardware con garantía 0."""
        # Creamos un item de Hardware con garantía 0
        item = frappe.get_doc({
            "doctype": "Item",
            "item_code": "TEST-ITEM-HW-0",
            "item_name": "Switch de Prueba",
            "item_group": "Hardware",
            "stock_uom": "Nos",
            "custom_warranty_period": 0
        })
        
        # No debe lanzar error (es solo una advertencia msgprint), pero debe insertarse correctamente
        item.insert()
        self.assertTrue(frappe.db.exists("Item", "TEST-ITEM-HW-0"))

    def test_customer_company_account_manager_warning(self):
        """PRUEBA: Validación de sugerencia de Gestor de Cuenta para Empresas."""
        customer = frappe.get_doc({
            "doctype": "Customer",
            "customer_name": "TEST-CUST-CORP",
            "customer_type": "Company",
            "customer_group": "Commercial",
            "territory": "Spain"
        })
        
        # Debe insertarse sin errores de validación (el msgprint no bloquea), 
        # pero la lógica de la función debe ser ejecutada.
        customer.insert()
        self.assertTrue(frappe.db.exists("Customer", "TEST-CUST-CORP"))

    def tearDown(self):
        """Limpieza final tras la ejecución de los tests."""
        frappe.db.rollback()
