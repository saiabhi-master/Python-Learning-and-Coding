from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

cdp = "/Users/abhinavavasarala/Downloads/Drivers_installs/chromedriver"
driver = webdriver.Chrome(executable_path=cdp)

URL = "https://www.linkedin.com/jobs/search/?currentJobId=3408756202&f_AL=true&f_BE=%5B%5D&f_C=%5B%5D&f_E=%5B%5D&f_EA=%5B%5D&f_F=%5B%5D&f_FCE=%5B%5D&f_I=%5B%5D&f_JC=%5B%5D&f_JIYN=%5B%5D&f_JT=%5B%5D&f_PP=%5B%5D&f_SB2=%5B%5D&f_T=%5B%5D&f_WT=%5B%5D&keywords=python%20developer&sortBy=R"
driver.get(URL)

sign_in = driver.find_element(By.XPATH, '/html/body/div[1]/header/nav/div/a[2]')
sign_in.click()

user_name = driver.find_element(By.ID, 'username')
user_name.send_keys("Saiabhinavavasarala@gmail.com")

pass_word = driver.find_element(By.ID, "password")
pass_word.send_keys("Saiabhi3690")

button = driver.find_element(By.CSS_SELECTOR, ".login__form_action_container button")
button.click()

time.sleep(1000)






