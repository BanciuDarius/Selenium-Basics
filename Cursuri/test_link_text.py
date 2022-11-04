from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#initializam un browser
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

chrome.get('https://formy-project.herokuapp.com/')
link = chrome.find_element(By.LINK_TEXT, "Autocomplete")
link.click()
sleep(5)
chrome.quit()