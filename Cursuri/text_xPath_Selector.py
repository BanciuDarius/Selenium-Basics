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

# Xpath -> recomandat - cel mai flexibil

# navigam catre un url
chrome.get('https://formy-project.herokuapp.com/form')

# selector by Xpath - atribut=valoare
chrome.find_element(By.XPATH, '//input[@id="first-name"]').send_keys('I')

# selector by Xpath - * toate elementele care resecta regula
chrome.find_element(By.XPATH, '//*[@id="first-name"]').send_keys('o')

# selector by Xpath - navigare in jos - trecem prin fiecare element
chrome.find_element(By.XPATH, '//div/div/input[@id="first-name"]').send_keys('a')

# selector by Xpath - navigare in jos - skip tags - cautam oriunde sub form un input care sa respecte regula
chrome.find_element(By.XPATH, '//form//input[@id="first-name"]').send_keys('n')

# selector by Xpath - selectare elem din lista - index incepe de la 1
chrome.find_element(By.XPATH, '(//input[@class="form-control"])[2]').send_keys('M')

sleep(3)

# selector by Xpath - OR primul gasit dintre variante
s = chrome.find_element(By.XPATH, '//input[@id="last-name1"] | //input[@id="last-name2"] | //input[@id="last-name"]')
# stergem valorile din input
s.clear()
s.send_keys('Morar')

# selector by Xpath - in f de textul partial + luam textul de pe el cu proprietatea text
full_text = chrome.find_element(By.XPATH, '//a[contains(text(), "Sub")]').text
print(full_text)
assert full_text == 'Submit'

sleep(3)

# selector by Xpath - in f de textul vizibil
# chrome.find_element(By.XPATH, '//a[text()="Submit"]').click()

'''
x y axis navigation
cu parent in sus
cu /elem_type - ajungem la elementul copil
cu //elem_type - cauta prin toti descendentii
cu parent::elem_type in sus
cu following-sibling::elem_type - urmatorul frate de la acelasi nivel
cu preceding-sibling::elem_type - fratele anterior de la acelasi nivel
//label[text()="First name"]/parent::strong/following-sibling::input/preceding-sibling::strong
'''


# cu ajutorul unei functii cand avem foarte multe elemente de acelasi tip
# si vrem sa parametrizam selectorul
def formy_input_by_placeholder(placeholder_text, input_value):
    input = chrome.find_element(By.XPATH, f'//input[@placeholder="{placeholder_text}"]')
    input.clear()
    input.send_keys(input_value)


def formy_input_by_label(label, input_value):
    my_input = chrome.find_element(By.XPATH, f'//label[text()="{label}"]/parent::strong/parent::div//input')
    my_input.clear()
    my_input.send_keys(input_value)


formy_input_by_placeholder('Enter first name', 'ION')
formy_input_by_placeholder('Enter last name', 'MORAR')

formy_input_by_label('Job title', 'Automation Engineer')

sleep(3)
chrome.quit()