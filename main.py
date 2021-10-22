import requests
from twilio.rest import Client
import os

# CONSTANTS
API_KEY = os.environ.get("API_KEY")
MY_LAT = os.environ.get("MY_LAT")
MY_LONG = os.environ.get("MY_LONG")
TO_PHONE = os.environ.get("TO_PHONE")
FROM_PHONE = os.environ.get("FROM_PHONE")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

# API PARAMETERS
parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "exclude": "current,minutely,daily",
    "appid": API_KEY
}

# API ACCESSING
response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()

# 12 HOUR WEATHER FORECAST ACCESS
is_going_to_rain = False
for x in range(0, 12):
    if weather_data["hourly"][x]["weather"][0]["id"] < 700:
        is_going_to_rain = True

# PRINT RESULT
if is_going_to_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today! Stay inside or bring an umbrella! Or maybe just play in the rain. :)",
        from_='+13524483943',
        to='+15126579803'
    )
    print(message.status)

