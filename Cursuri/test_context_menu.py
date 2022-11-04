from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#initializam un browser
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

chrome.get("https://the-internet.herokuapp.com/context_menu")
action = ActionChains(chrome)
action.context_click(chrome.find_element(By.CSS_SELECTOR, "[oncontextmenu ='displayMessage()")).perform()
sleep(5)