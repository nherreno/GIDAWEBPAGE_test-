import csv
import yaml
import os

def limpiar_y_convertir(nombre_archivo):
    ruta_csv = f'_data/{nombre_archivo}.csv'
    ruta_yml = f'_data/{nombre_archivo}.yml'
    
    if not os.path.exists(ruta_csv):
        return

    # Intentamos leer con la codificación de Excel (cp1252) que es la que suele traer tildes
    # Si falla, intenta con utf-8. 'replace' ignora caracteres que no entiende en vez de dar error.
    datos = []
    for encoding_intento in ['cp1252', 'utf-8', 'latin-1']:
        try:
            with open(ruta_csv, mode='r', encoding=encoding_intento, errors='replace') as f:
                # Detectamos si usas comas o puntos y comas (Excel a veces cambia esto)
                contenido = f.read(2048)
                f.seek(0)
                dialecto = csv.Sniffer().sniff(contenido)
                lector = csv.DictReader(f, dialect=dialecto)
                datos = [fila for fila in lector]
                if datos: break 
        except:
            continue

    if datos:
        with open(ruta_yml, 'w', encoding='utf-8') as f:
            yaml.dump(datos, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
        print(f"✅ Procesado con éxito: {nombre_archivo}")

if __name__ == "__main__":
    limpiar_y_convertir('convocatorias')
    # Si tienes el de miembros, descomenta la siguiente línea:
    # limpiar_y_convertir('miembros')