import os, requests, csv

def ejecutar():
    BASE_ID = "appqzHunqskWZJNc2"
    TABLE_ID = "tblWiTUee1VWK9OZ2"
    TOKEN = os.environ.get("AIRTABLE_API")
    
    url = f"https://api.airtable.com/v0/{BASE_ID}/{TABLE_ID}"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    
    response = requests.get(url, headers=headers)
    data = response.json()

    if "records" not in data:
        print("Error:", data)
        return

    # Extraemos los datos de cada fila
    filas = []
    for r in data["records"]:
        filas.append(r["fields"])

    if filas:
        # Usamos las llaves de la primera fila como nombres de columna
        columnas = filas[0].keys()
        with open("datos_censo.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=columnas)
            writer.writeheader()
            writer.writerows(filas)
        print("¡Archivo creado!")

if name == "main":
    ejecutar()
