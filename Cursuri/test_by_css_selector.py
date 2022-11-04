# avem nevoie sa importam cateva librarii gratuite care ne ajuta sa controlam chrome
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# initializam chrome
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

# maximizam fereastra
chrome.maximize_window()

# navigam catre un url
chrome.get('https://formy-project.herokuapp.com/form')

# selector by CSS - ID
chrome.find_element(By.CSS_SELECTOR, 'input#first-name').send_keys('Pet')

# selector by CSS - Class - only first one if multiple matches
chrome.find_element(By.CSS_SELECTOR, 'input.form-control').send_keys('ruta')

# selector by CSS - atribut=valoare
chrome.find_element(By.CSS_SELECTOR, 'input[placeholder="Enter last name"]').send_keys('m')

# selector by CSS - atribut=valoare partiala + parinte -> copil
chrome.find_element(By.CSS_SELECTOR, 'div input[placeholder*="last name"]').send_keys('orar')


sleep(3)
chrome.quit()