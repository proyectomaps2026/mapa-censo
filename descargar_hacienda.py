import os
import requests
import csv

# Configuración con tus IDs exactos
BASE_ID = "appqzHunqskWZJNc2"
TABLE_ID = "tblWiTUee1VWK9OZ2"
TOKEN = os.environ.get("AIRTABLE_API")

def ejecutar():
    url = f"https://api.airtable.com/v0/{BASE_ID}/{TABLE_ID}"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    
    response = requests.get(url, headers=headers)
    data = response.json()

    if "records" not in data:
        print("Error en Airtable:", data)
        return

    # Extraer los datos
    registros = [r["fields"] for r in data["records"]]
    if not registros:
        print("No hay datos en la tabla")
        return

    # Obtener los nombres de las columnas
    columnas = registros[0].keys()

    # Guardar como CSV
    with open("datos_censo.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=columnas)
        writer.writeheader()
        writer.writerows(registros)
    print("¡CSV creado con éxito!")

if name == "main":
    ejecutar()
