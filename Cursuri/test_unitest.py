import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Test(unittest.TestCase):
    # elementele din pagina
    # in loc sa le scriem de n ori in teste, le trecem aici o sg data
    SUBMIT_BTN = (By.XPATH, '//a[@role="button"]')
    FIRST_NAME_INPUT = (By.XPATH, '//input[@id="first-name"]')
    MIDDLE_NAME_INPUT = (By.XPATH, '//input[@id="middle-name"]')
    chrome = None

    # se rulaza inainte de fiecare test
    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://formy-project.herokuapp.com/form')

    # se ruleaza dupa fiecare test
    def tearDown(self):
        self.chrome.quit()

    # verificam URL
    def test_url(self) -> None:
        actual = self.chrome.current_url
        expected = 'https://formy-project.herokuapp.com/form'
        # expected value, actual value, mesaj in caz de fail
        self.assertEqual(expected, actual, 'URL is incorrect')

    # verificam page title
    def test_page_title(self):
        actual = self.chrome.title
        expected = 'Formy2'
        self.assertEqual(expected, actual, 'Page title is incorrect')

    # verificam text de pe element (buton, mesaj de eroare etc)
    def test_submit_btn_text(self):
        # * tuple unpacking - se ia valoarea din tuple si se da ca argument in functie
        actual = self.chrome.find_element(*self.SUBMIT_BTN).text
        expected = 'Submit'
        self.assertEqual(expected, actual, 'Submit btn text is incorrect')

    # verificam ca element e vizibil
    @unittest.skip('Not ready yet')
    def test_elem_visible(self):
        elem = self.chrome.find_element(*self.SUBMIT_BTN)
        self.assertTrue(elem.is_displayed(), 'Submit btn nu e vizibil')

    # verificam ca element are un atribut asteptat (ex clasa)
    @unittest.skip('Not ready yet')
    def test_elem_atribute(self):
        actual = self.chrome.find_element(*self.SUBMIT_BTN).get_attribute('class')
        expected = 'btn btn-lg btn-primary'
        self.assertEqual(expected, actual, 'Submit btn href attribute is wrong')

    # verificam ca element nu e prezent
    @unittest.skip('Not ready yet')
    def test_elem_not_displayed(self):
        # ai zice ca merge asa dar nu
        # middle_name = self.chrome.find_element(*self.MIDDLE_NAME_INPUT)
        # self.assertFalse(middle_name.is_displayed(), 'Mid name e vizibil')
        pass

    # verificam ca element nu e prezent v1
    @unittest.skip('Not ready yet')
    def test_elem_not_displayed_v1(self):
        # verificam ca lista e goala
        middle_name = self.chrome.find_elements()
        self.assertTrue(len(middle_name) == 0, 'Mid name e vizibil in mod incorect')

    # verificam ca element nu e prezent v2
    @unittest.skip('Not ready yet')
    def test_elem_not_displayed_v2(self):
        # verificam ca apare exceptia NoSuchElementException
        try:
            self.chrome.find_element(*self.MIDDLE_NAME_INPUT)
        except NoSuchElementException:
            pass

    # waits pe url
    @unittest.skip('Not ready yet')
    def test_url_waits(self):
        self.chrome.find_element(*self.SUBMIT_BTN).click()
        # asteptam ca fostul url sa se schimbe
        WebDriverWait(self.chrome, 5).until(EC.url_changes('https://formy-project.herokuapp.com/form'))
        # asteptam ca noul url sa contina
        WebDriverWait(self.chrome, 5).until(EC.url_contains('/thanks'))
        # asteptam ca noul url sa fie exact
        WebDriverWait(self.chrome, 5).until(EC.url_to_be('https://formy-project.herokuapp.com/thanks'))

        # daca in 5 secunde nu ajungem pe url corect putem
        try:
            WebDriverWait(self.chrome, 5).until(EC.url_contains('/thanks2'))
        except TimeoutException:
            self.assertTrue(False, 'Am asteptat 5 secunde dar url nu se incarca sau nu e corect')