import csv
import yaml
import os

def csv_to_yaml(filename):
    csv_path = f'_data/{filename}.csv'
    yaml_path = f'_data/{filename}.yml'
    
    if not os.path.exists(csv_path):
        print(f"Archivo {csv_path} no encontrado.")
        return

    # Intentamos varias codificaciones por si Excel lo guardó raro
    encodings = ['utf-8', 'latin-1', 'cp1252']
    data = None
    
    for enc in encodings:
        try:
            with open(csv_path, 'r', encoding=enc) as f:
                reader = csv.DictReader(f)
                data = list(reader)
                break
        except Exception:
            continue

    if data:
        with open(yaml_path, 'w', encoding='utf-8') as f:
            yaml.dump(data, f, allow_unicode=True, sort_keys=False)
        print(f"✅ {filename}.yml generado con éxito.")

if __name__ == "__main__":
    csv_to_yaml('convocatorias')