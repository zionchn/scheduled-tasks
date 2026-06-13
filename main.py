import os
import requests
from twilio.rest import Client

API_KEY = os.environ.get("OWM_API_KEY") # Your API key
MY_LAT = 9.076479 # Your latitude
MY_LONG = 7.398574 # Your longitude
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "cnt": 4,
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()

weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain buddy, bring an umbrella☔️",
        from_="whatsapp:+14155238886",
        to="whatsapp:+2348039125205",
    )

print(message.body)

