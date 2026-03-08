import csv
import yaml
import os

def procesar_archivo(nombre):
    csv_file = f'_data/{nombre}.csv'
    yml_file = f'_data/{nombre}.yml'
    
    if not os.path.exists(csv_file):
        print(f"⚠️ No se encontro {csv_file}")
        return

    # Intentar leer el CSV con diferentes codificaciones (latinoamerica/excel)
    encodings = ['utf-8', 'latin-1', 'cp1252', 'utf-8-sig']
    for enc in encodings:
        try:
            with open(csv_file, mode='r', encoding=enc) as f:
                # Usamos el delimitador automático por si Excel usa punto y coma
                dialect = csv.Sniffer().sniff(f.read(1024))
                f.seek(0)
                reader = csv.DictReader(f, dialect=dialect)
                datos = [row for row in reader]
                
            # Guardar como YAML en formato limpio
            with open(yml_file, 'w', encoding='utf-8') as f:
                yaml.dump(datos, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
            print(f"✅ Convertido: {nombre}.csv -> {nombre}.yml")
            return
        except Exception as e:
            continue
    print(f"❌ Error fatal procesando {nombre}.csv")

if __name__ == "__main__":
    procesar_archivo('convocatorias')
    procesar_archivo('miembros')