from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#initializam un browser
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

chrome.get('https://formy-project.herokuapp.com/form')
input = chrome.find_element(By.TAG_NAME, "input")
input.send_keys("petruta")
list_inputs = chrome.find_elements(By.TAG_NAME, "input")
list_inputs[2].send_keys("qa")
sleep(5)
chrome.quit()