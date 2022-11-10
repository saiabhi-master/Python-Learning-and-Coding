import requests
import datetime as dt
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPKEY = "alpha key"
#-------
FULL_KEY_ALP = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=TSLA&interval=60min&apikey={ALPKEY}"
NEWS_API_KEY = "news api key"
#-------

#twilio:
account_sid = "account sid"
auth_token = "auth token"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
URL = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={STOCK}&interval=60min&apikey={ALPKEY}'
r = requests.get(url=URL)
data = r.json()

#take a look at starting and ending price of day, and see the difference
#time module:
now = dt.datetime.now()
yd = str(int(now.day) - 1)
dbyd = str(int(yd) - 1)
month = now.month
year = now.year


def add_zero(numy):
    if len(numy) == 1:
        numb = "0" + numy
        return numb

yesterday = add_zero(yd)
day_before = add_zero(dbyd)

def make_date(when, time):
    global yesterday
    global day_before
    global year
    global month

    if when == "oneday":
        return (f"{year}-{month}-{yesterday} {time}:00:00")
    else:
        return (f"{year}-{month}-{day_before} {time}:00:00")


def change(x, y):
    x_num = float(x)
    y_num = float(y)
    changein = y_num - x_num
    percent_change = float(changein/x_num)
    return round(percent_change * 100 )

#stock market from 5:00:00 to 20:00:00
starting_price = data["Time Series (60min)"][make_date("oneday", "05")]["1. open"]
closing_price = data["Time Series (60min)"][make_date("oneday", "20")]["4. close"]




## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
news_url = f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&from=2022-11-08&sortBy=popularity&apiKey={NEWS_API_KEY}"

news_request = requests.get(url=news_url)
news_data = news_request.json()
information = news_data["articles"][0]["description"]

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the2percentage change and each article's title and description to your phone number.
if abs(change(starting_price, closing_price)) >= 5:
    num_change = change(starting_price, closing_price)
    print("Absolute change more than 5% !")
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=f"Your {COMPANY_NAME} stock price has change by {num_change}%\n{information}",
        from_="(858) 330-0718",
        to="+19199167686",
    )
    print(message.status)


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""







