from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from unittest import TestCase


class Login(TestCase):
    ACCEPT_BTN = (By.XPATH, '//*[@id="gdprCookieBar"]//*[@class="action primary"]')
    CONNECT = (By.ID, 'authorization-trigger')
    USER = (By.ID, 'email')
    PAROLA = (By.NAME, 'login[password]')
    CONNECT_BTN = (By.XPATH, '//*[@id="send2"]')
    DELOGARE_BTN = (By.ID, 'authorization-trigger')
    LOGOUT = (By.XPATH, '//*[@id="cdz-login-form-dropdown"]//*[@class="log-out link"]')
    ERR_MSG = (By.XPATH, "//div[@data-ui-id='message-error']")



    def setUp(self) -> None:
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://www.daciaplant.ro/')

    def tearDown(self) -> None:
        self.chrome.quit()

    def test_check_daciaplant_url(self):
        actual = self.chrome.current_url
        expected = 'https://www.daciaplant.ro/'
        self.assertEqual(actual, expected, 'The page is not correct')
        sleep(2)

    def test_login(self):
        # verif ca se intra pe site si se accepta cookie
        self.chrome.implicitly_wait(10)
        self.chrome.find_element(*self.ACCEPT_BTN).click()
        # se verif ca se face logarea cu datele corecte
        self.chrome.find_element(*self.CONNECT).click()
        self.chrome.find_element(*self.USER).send_keys('irinavoinea@yahoo.com')
        self.chrome.find_element(*self.PAROLA).send_keys('irinairina')
        self.chrome.find_element(*self.CONNECT_BTN).click()
        actual = self.chrome.current_url
        expected = 'https://www.daciaplant.ro/customer/account/'
        print('contul a fost creat cu succes')
        self.assertEqual(actual, expected, 'contul a fost creat cu succes')


    def test_logout(self):
        # verif ca se face ok delogarea din cont
        self.chrome.implicitly_wait(10)
        self.chrome.find_element(*self.ACCEPT_BTN).click()
        self.chrome.find_element(*self.CONNECT).click()
        self.chrome.find_element(*self.USER).send_keys('irinavoinea@yahoo.com')
        self.chrome.find_element(*self.PAROLA).send_keys('irinairina')
        self.chrome.find_element(*self.CONNECT_BTN).click()
        self.chrome.find_element(*self.DELOGARE_BTN).click()
        self.chrome.find_element(*self.LOGOUT).click()
        expected_text = 'CONECTARE'
        actual_text = self.chrome.find_element(*self.CONNECT).text
        assert expected_text in actual_text, 'Nu, m-am delogat'



    def test_login_invalid_password(self):
        # se verif ca afiseaza mesaj de err daca se introd parola gresita
        self.chrome.implicitly_wait(10)
        self.chrome.find_element(*self.ACCEPT_BTN).click()
        self.chrome.find_element(*self.CONNECT).click()
        self.chrome.find_element(*self.USER).send_keys('irinavoinea@yahoo.com')
        self.chrome.find_element(*self.PAROLA).send_keys('123456789')
        self.chrome.find_element(*self.CONNECT_BTN).click()
        asteptare_eroare = WebDriverWait(self.chrome, 10).until(EC.presence_of_element_located(self.ERR_MSG))
        mes = 'The account sign-in'
        if mes in asteptare_eroare.text:
            print('Mesajul de eroare este afisat')
        else:
            print('mesajul de err nu este afisat')
        assert mes in asteptare_eroare.text