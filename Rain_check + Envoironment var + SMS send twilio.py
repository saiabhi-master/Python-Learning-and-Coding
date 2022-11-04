import os
import requests
from twilio.rest import Client

api_key = "9b61a8402c5c5c2fc5fc3aad2fb84dbe"
endpoint = "http://api.openweathermap.org/data/2.5/forecast"
account_sid = "AC37cf3afcd1f2c87a0bee46f9df8e5369"
auth_token = "36f4efd527af3fa897105ee0d496f7d1"

weather_parameters = {
    "lat": 39.099728,
    "lon": -94.578568,
    "appid": api_key,

}
response = requests.get(endpoint, params=weather_parameters)
data = response.json()

weather_ids = []


useful_data = data["list"][0:5]
for i in range(0, 5):
    id = useful_data[i]["weather"][0]["id"]
    weather_ids.append(id)
print(weather_ids)

for i in weather_ids:
    rain = False
    if i < 800:
        rain = True

#SEND SMS ( Using - Twilio API )

if rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today, bring an umbrella to be safe!",
        from_="(858) 330-0718",
        to = "+19199167686",
    )
    print(message.status)
else:
    print("wohoo! No rain")


#Environment KeysSSSSSSS

# first ( import os )
# export API_KEY=6787878(whatever is the value) - in the console
# hit env in the console
# in code: api_key = os.environ.get("API_KEY")
# when running in python everywhere:
# export API_KEY=value; export anothervariable=value(if exists); python3.10 main.py







