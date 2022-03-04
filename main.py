import requests
import os
from dotenv import load_dotenv
load_dotenv()


OWM_Endpoint=os.getenv("END_POINT")
api_key=os.getenv("API_KEY")
parametros={
    "lat":19.432608,
    "lon":-99.133209,
    "appid":api_key,
    "exclude":"current,minutely,daily"
}

response=requests.get(OWM_Endpoint,params=parametros)
response.raise_for_status()
datos=response.json()
primeros_12=datos["hourly"][:12]

llovera=False
for hora in primeros_12:
    cod_clima=hora["weather"][0]["id"]

    if int(cod_clima)<700:
        llovera=True

if llovera:
    print("Lleva una sombilla")
else:
    print("No llevará no lleves paraguas")



# print(datos["hourly"][0]["weather"][0]["id"])