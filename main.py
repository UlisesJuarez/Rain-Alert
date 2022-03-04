from twilio.rest import Client
import requests
import os
from dotenv import load_dotenv
load_dotenv()


OWM_Endpoint = os.getenv("END_POINT")
api_key = os.getenv("API_KEY")
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
my_number=os.getenv("PHONE")


parametros = {
    "lat": 19.432608,
    "lon": -99.133209,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=parametros)
response.raise_for_status()
datos = response.json()
primeros_12 = datos["hourly"][:12]

llovera = False
for hora in primeros_12:
    cod_clima = hora["weather"][0]["id"]

    if int(cod_clima) < 700:
        llovera = True

if llovera:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It's going to rain today. Remember to bring an umbrella",
            from_='+17622165590',
            to=my_number
        )
    print(message.status)
else:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It isn't going to rain today. Don't bring an umbrella",
            from_='+17622165590',
            to=my_number
        )
    print(message.status)
