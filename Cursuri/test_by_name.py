from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#initializam un browser
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

chrome.get('http://www.seleniumframework.com/Practiceform/')
country_input = chrome.find_element(By.NAME, "country")
country_input.send_keys("romania")
company_input = chrome.find_element(By.NAME, "company")
company_input.send_keys("it factory")
sleep(5)
chrome.quit()