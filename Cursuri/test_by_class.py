from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#initializam un browser
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

chrome.get('https://formy-project.herokuapp.com/buttons')
success_button = chrome.find_element(By.CLASS_NAME, "btn-success")
success_button.click()
sleep(5)
chrome.quit()