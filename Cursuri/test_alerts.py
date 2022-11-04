from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#initializam un browser
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

chrome.get("https://the-internet.herokuapp.com/javascript_alerts")
alert = chrome.find_element(By.CSS_SELECTOR, "[onclick='jsAlert()']")
alert.click()
alerta = chrome.switch_to.alert
alerta.accept()
result = chrome.find_element(By.ID, "result")
assert "You successfully clicked an alert" == result.text
confirm = chrome.find_element(By.CSS_SELECTOR, "[onclick='jsConfirm()']")
confirm.click()
sleep(10)
alerta = chrome.switch_to.alert
alerta.dismiss()
assert "You clicked: Cancel" == result.text
sleep(10)
prompt = chrome.find_element(By.CSS_SELECTOR, "[onclick='jsPrompt()']")
prompt.click()
alerta = chrome.switch_to.alert
alerta.send_keys("MAMA")
alerta.accept()
assert "You entered: MAMA" == result.text
sleep(10)
chrome.quit()