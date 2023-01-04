import requests
import smtplib
import lxml
from bs4 import BeautifulSoup

my_email = "testingtester3690@gmail.com"
password = "gidv heet lqys kdss"

URL = "https://www.amazon.com/COSORI-1700-Watt-Cookbook-One-Touchscreen-Customizable/dp/B085W3GN5J/ref=sr_1_2_sspa?crid=XSFFSE0DS6EE&keywords=air%2Bfryer&qid=1671638493&s=home-garden&sprefix=air%2Bfryer%2Cgarden%2C85&sr=1-2-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExU1c3MVcxVVY0T0tBJmVuY3J5cHRlZElkPUEwMjA1OTcwMlA2VEVHSjlNQ1dQNiZlbmNyeXB0ZWRBZElkPUEwODgwNjkwMzA2UDk2SDY2RFpUQSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU&th=1"

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
accept_language = "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7"

r = requests.get(URL, headers={"Accept-Language": accept_language, "User-Agent": user_agent})
soup = BeautifulSoup(r.content, "lxml")

price = soup.find(class_="a-price-whole").get_text()
x = price.split(".")
number = float(x[0])


if number < 70:
    with (smtplib.SMTP("smtp.gmail.com", port=587)) as connection:  # establishing connection
        connection.starttls()
        # way of securing connection to email server
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="testingtester3690@yahoo.com",
                            msg=f"Subject:Low Price Alert!\n\nThe item that you have wanted is available at a much lower price of ${number}.\nHere is the link: {URL}")



