from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#initializam un browser
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

chrome.get("https://the-internet.herokuapp.com/login")
username_input = chrome.find_element(By.ID, "username")
# username_input.send_keys("DVFDVfd")
# password_input = chrome.find_element(By.ID, "password")
# password_input.send_keys("DVFDVfd")
# password_input.send_keys(Keys.ENTER)
sleep(10)
username_input.send_keys("DVFDVfd")
sleep(10)
username_input.send_keys(Keys.CONTROL + 'a')
username_input.send_keys(Keys.BACKSPACE)
sleep(10)
chrome.quit()