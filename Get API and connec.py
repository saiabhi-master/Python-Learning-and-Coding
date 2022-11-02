import smtplib
import time

import requests
from datetime import datetime

EMAIL = "testingtester3690@"
PASS = "gidv heet lqvs kdss"

MY_LAT = 35.791470 # Your latitude
MY_LONG = -78.781143 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
def in_pos():
    global iss_longitude
    global iss_latitude
    global MY_LAT
    global MY_LONG

    if abs(iss_latitude - MY_LAT) <= 5:
        if abs(iss_longitude - MY_LONG) <= 5:
            return True
        else:
            return False
    else:
        return False

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])



time_now = datetime.now()
hour = time_now.hour

def is_night():
    global sunrise
    global sunset
    global hour

    if hour < sunrise or hour > sunset:
        return True
    else:
        return False

while True:
    time.sleep(60)
    if in_pos() and is_night():
        connection = smtplib.SMTP()
        connection.login(EMAIL, PASS)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg="Subject:Look Up\n\nThe ISS is above you in the sky"
        )



#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



