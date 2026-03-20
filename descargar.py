import os
import requests
import pandas as pd

# Datos de tu cuenta (no cambies esto)
BASE_ID = "appqzHunqskWZJNc2"
TABLE_ID = "tblWiTUee1VWK9OZ2"
TOKEN = os.environ.get("AIRTABLE_API")

def descargar_datos():
    url = f"https://api.airtable.com/v0/{BASE_ID}/{TABLE_ID}"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    
    params = {}
    records = []
    
    while True:
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        
        if "records" not in data:
            print("Error en la respuesta:", data)
            break
            
        for record in data["records"]:
            # Extrae los datos de las columnas
            row = record["fields"]
            records.append(row)
            
        if "offset" in data:
            params["offset"] = data["offset"]
        else:
            break
            
    # Crea el CSV
    df = pd.DataFrame(records)
    df.to_csv("datos_censo.csv", index=False)
    print("CSV creado exitosamente")

if name == "main":
    descargar_datos()
