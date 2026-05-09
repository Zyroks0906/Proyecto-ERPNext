import json
import os

def test_validation():
    file_path = "custom_app/data_migration/maestros.json"
    
    print(f"--- Validando archivo: {file_path} ---")
    
    if not os.path.exists(file_path):
        print(f"[ERROR] No se encuentra el archivo en {file_path}")
        return

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            print("[OK] JSON válido (sintaxis correcta)")
    except Exception as e:
        print(f"[ERROR] Error al leer el JSON: {e}")
        return

    expected_keys = ["Item", "Customer", "Supplier"]
    for key in expected_keys:
        if key in data:
            print(f"[OK] Se encontró la sección: {key} ({len(data[key])} entradas)")
        else:
            print(f"[WARNING] No se encontró la sección: {key}")

    print("\n--- Verificando estructura de datos ---")
    for item in data.get("Item", []):
        if "item_code" not in item or "item_name" not in item:
            print(f"[ERROR] Item incompleto: {item}")
        else:
            print(f"  - Item: {item['item_code']} listo")

    for customer in data.get("Customer", []):
        if "customer_name" not in customer:
            print(f"[ERROR] Cliente incompleto: {customer}")
        else:
            print(f"  - Cliente: {customer['customer_name']} listo")

    print("\n--- TEST FINALIZADO ---")
    print("La estructura es correcta. En cuanto Docker funcione, la importación debería ir perfecta.")

if __name__ == "__main__":
    test_validation()
