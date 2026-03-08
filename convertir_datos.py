import csv
import yaml
import os

def csv_to_yaml(filename):
    csv_path = f'_data/{filename}.csv'
    yaml_path = f'_data/{filename}.yml'
    
    if not os.path.exists(csv_path):
        return

    with open(csv_path, 'r', encoding='latin-1') as f: # Soporta el Excel "a las malas"
        reader = csv.DictReader(f)
        data = list(reader)

    with open(yaml_path, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, allow_unicode=True, sort_keys=False)

# Convertimos ambos archivos
csv_to_yaml('convocatorias')
csv_to_yaml('miembros')