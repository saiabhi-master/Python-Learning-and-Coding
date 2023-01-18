from bs4 import BeautifulSoup
import smtplib
import lxml
import requests


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

URL = 'https://www.zillow.com/cary-nc/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22Cary%2C%20NC%22%2C%22mapBounds%22%3A%7B%22west%22%3A-79.06641920019531%2C%22east%22%3A-78.59263379980469%2C%22south%22%3A35.62577108511695%2C%22north%22%3A35.95161085842931%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A51297%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A872627%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min%22%3A2%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D'
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
accept_language = "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7"

response = requests.get(URL, headers={"Accept-Language": accept_language, "User-Agent": user_agent})

page = response.content

soup = BeautifulSoup(page, "lxml")

price_data_spans = soup.select('.StyledPropertyCardDataArea-c11n-8-81-1__sc-yipmu-0.wgiFT span')
address_data_spans = soup.select('.StyledPropertyCardDataArea-c11n-8-81-1__sc-yipmu-0.lpqUkW.property-card-link address')
links_data_spans = soup.select("a.property-card-link")


def strip_price(data):
    x = data.split("+")
    return x[0]

def add_zillow(data):
    x = "zillow.com" + data["href"]
    return x

prices_data = [strip_price(span.text) for span in price_data_spans]
address_data = [data.text for data in address_data_spans]
links_data = [add_zillow(data) for data in links_data_spans]

#------------------------------------------

cdp = "/Users/abhinavavasarala/Downloads/Drivers_installs/chromedriver"
driver = webdriver.Chrome(executable_path=cdp)

URL_2 = 'https://docs.google.com/forms/d/e/1FAIpQLSd7MAOdx_Hh7Y3EpNJGPdwNbSTOr0f8a8SVj0yZla_t3mZwsw/viewform'
driver.get(URL_2)

address_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
price_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
link_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

# for i in range(prices_data):
#     price = prices_data[i]
#     address = address_data[i]
#     link = links_data[i]
sign_in_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[3]/div[2]/span/span')
sign_in_button.click()
time.sleep(2)

email_input = driver.find_element(By.XPATH, '//*[@id="identifierId"]')
email_input.send_keys("Saiabhi3690@gmail.com")
next_button = driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span')
next_button.click()

time.sleep(1000)
address_input.send_keys("abhi")
price_input.send_keys("baba")
link_input.send_keys("ww.gogl")

time.sleep(1000)



