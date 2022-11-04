from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#initializam un browser
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

chrome.get('https://www.emag.ro')
# my_account_button = chrome.find_element(By.CSS_SELECTOR, "[class = 'em em-user2 navbar-icon']")
# my_account_button = chrome.find_element(By.CSS_SELECTOR, "a#my_account > i")
# my_account_button = chrome.find_element(By.CSS_SELECTOR, "ul.megamenu-list li:first-child a> i")
my_account_button = chrome.find_element(By.XPATH, "//a[@id='my_account']/i")
my_account_button2 = chrome.find_element(By.XPATH, "//ul[@class='megamenu-list']/li[1]/a/i")
#* contine
#$ se termina cu textul ala
#^ incepe cu textul ala

sleep(5)
chrome.quit()