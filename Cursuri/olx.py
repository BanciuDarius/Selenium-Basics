import unittest
from time import sleep
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC



class Olx(unittest.TestCase):
    EMAIL_INPUT = (By.XPATH, '//input[@name="login[email]"][1]')
    PAROLA_INPUT = (By.XPATH, '//input[@name="login[password]"]')
    INTRA_IN_CONT_BUTTON = (By.XPATH, '//button[@id="se_userLogin"][1]')
    ERROR_EMAIL = (By.XPATH, '//label[@class="error"]')
    SEARCH_FIELD = (By.XPATH, '//input[@id="headerSearch"]')
    CAUTA_ACUM_BUTTON = (By.XPATH, '//input[@id="submit-searchmain"]')
    ADAUGA_UN_ANUNT_BUTTON = (By.XPATH,'//a[@id="postNewAdLink"]')
    ACCEPT_COOKIES = (By.XPATH, '//button[@id="onetrust-accept-btn-handler"]')




    def setUp(self):
        # s = Service(ChromeDriverManager().install())
        #self.browser = webdriver.Chrome(service = s)
        self.browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.browser.maximize_window()
        self.browser.get('https://www.olx.ro/')
        self.browser.implicitly_wait(10)
        self.browser.find_element(By.XPATH, '//button[@id="onetrust-accept-btn-handler"]').click()






    def tearDown(self):
        self.browser.quit()

    def test_cookies(self):
        try:
            self.browser.find_element(*self.ACCEPT_COOKIES).click()
        except NotImplementedError:
                # NoSuchElementException:
            pass

    def test_URL(self):
        actual=self.browser.current_url
        expected = 'https://www.olx.ro/'
        self.assertEqual(expected,actual, 'URL Error')

    def test_search_field(self):
        field = self.browser.find_element(*self.SEARCH_FIELD)
        self.assertTrue(field.is_displayed, 'Search field display error ')

    def test_cauta_acum_button(self):
        button = self.browser.find_element(*self.CAUTA_ACUM_BUTTON)
        self.assertTrue(button.is_displayed(), 'No button visible')


    def test_no_ads(self):
        self.browser.find_element(*self.SEARCH_FIELD).send_keys('cursuri testare automata')
        self.browser.find_element(*self.CAUTA_ACUM_BUTTON).click()
        message = self.browser.find_element(By.XPATH,'//span[@class="marker"]/parent::p[contains(text(), Nu)]')
        self.assertTrue(message.is_displayed(), 'There is at least one ad' )

    def test_new_add(self):
        button = self.browser.find_element(*self.ADAUGA_UN_ANUNT_BUTTON)
        self.assertTrue(button.is_displayed(), 'No such button displayed')

    def test_login_error(self):
        sleep(2)
        self.browser.find_element(*self.ADAUGA_UN_ANUNT_BUTTON).click()
        sleep(2)
        self.browser.find_element(*self.INTRA_IN_CONT_BUTTON).click()
        sleep(2)
        self.browser.find_element(*self.EMAIL_INPUT).clear()
        self.browser.find_element(*self.PAROLA_INPUT).clear()
        error = self.browser.find_element(*self.ERROR_EMAIL)
        self.assertTrue(error.is_displayed(),'No error message')