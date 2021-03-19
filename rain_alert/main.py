import requests
import os
from twilio.rest import Client

# Get  api_key from https://openweathermap.org
api_key = ""
lat = 35.370022
lon = 1.322750

# Get  account_sid and auth_token from twilio.com
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

weather_params = {
    "lat": lat,
    "lon": lon,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=weather_params)
response.raise_for_status()
data = response.json()
weather_slice = data["hourly"][:12]
will_rain = False
for hour in weather_slice:
    weather_condition = hour["weather"][0]["id"]
    if weather_condition < 600:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today! take an umbrella ☔️",
        from_='+19473334519',
        # your verified number on twilio
        to='+213 xxx xx xx xx'
    )

    print(message.status)

# Run the main.py on https://www.pythonanywhere.com to get notification at a specific time everyday
