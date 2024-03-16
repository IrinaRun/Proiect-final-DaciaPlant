from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager import chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from unittest import TestCase
import unittest

class Add_to_cart(TestCase):
    ACCEPT_BTN = (By.XPATH, '//*[@id="gdprCookieBar"]//*[@class="action primary"]')
    CONNECT = (By.ID, 'authorization-trigger')
    CATEG_ANTISTRES = (By.XPATH, "//span[text() = 'Antistres']")
    MENU_LINK = (By.XPATH, "//span[text() = 'La ce folosesc']")
    INSOMNIE = (By.XPATH, "//*[text()='Insomnie  ']")
    PRODUSE_INSOMNIE = (By.XPATH, '//*[@id="category-products-grid"]//li[@class = "item product product-item"]')
    ALEGE_PROD = (By.XPATH, '// *[@id ="category-products-grid"]//li[@class="item product product-item"][2]'
                            '//*[@class="product details product-item-details mf-initial"]')
    ADAUGA_COS = (By.ID, 'product-addtocart-button')
    MESAJ_SUCCES = (By.XPATH, '// *[ @ id = "maincontent"] / div[1] / div[2] / div / div / div')
    COS= (By.XPATH,'//*[@class="action showcart"]')
    STERGERE = (By.XPATH,'//*[@id="shopping-cart-table"]//*[@class="action action-delete"]')
    MES_STERGERE = (By.XPATH,'// *[ @ id = "maincontent"] // *[ @class ="cart-empty mf-initial"]')
    FAVORITE = (By.XPATH,'//*[@id="product_addtocart_form"]/div[2]/a/span')
    MESAJ_FAVORITE =(By.XPATH,'//*[@id="maincontent"]/div[1]/div[2]/div/div/div')
    USER = (By.ID, 'email')
    PAROLA = (By.NAME, 'login[password]')
    CONNECT_BTN = (By.XPATH, '//*[@id="send2"]')

    def setUp(self) -> None:
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://www.daciaplant.ro/')

    def tearDown(self) -> None:
        self.chrome.quit()

    def test_place_into_cart(self):
        #se verifica ca se poate adauga un produs in cos
        self.chrome.implicitly_wait(10)
        self.chrome.find_element(*self.ACCEPT_BTN).click()
        self.chrome.find_element(*self.MENU_LINK).click()
        self.chrome.find_element(*self.CATEG_ANTISTRES).click()
        self.chrome.find_element(*self.INSOMNIE).click()
        self.chrome.find_element(*self.ALEGE_PROD).click()
        self.chrome.find_element(*self.ADAUGA_COS).click()
        adaugat = self.chrome.find_element(*self.MESAJ_SUCCES).text
        expected = 'Ati adaugat Valeriana tinctura fara alcool '
        assert expected in adaugat, (f"Textul afișat este diferit de cel așteptat. Așteptat: "
                                    f"'{expected}', Obținut: '{adaugat}'")


    def test_delete_from_cart(self):
        #se testeaza ca se poate sterge un produs din cos
        self.chrome.implicitly_wait(10)
        self.chrome.find_element(*self.ACCEPT_BTN).click()
        self.chrome.find_element(*self.MENU_LINK).click()
        self.chrome.find_element(*self.CATEG_ANTISTRES).click()
        self.chrome.find_element(*self.INSOMNIE).click()
        self.chrome.find_element(*self.ALEGE_PROD).click()
        self.chrome.find_element(*self.ADAUGA_COS).click()
        self.chrome.find_element(*self.COS).click()
        self.chrome.find_element(*self.STERGERE).click()
        mesaj='Nu exista produse in cos.'
        expected = self.chrome.find_element(*self.MES_STERGERE).text
        assert mesaj in expected


    def test_add_to_favorites(self):
        #se testeaza ca se poate adauga un produs la Favorite
        self.chrome.implicitly_wait(10)
        self.chrome.find_element(*self.ACCEPT_BTN).click()
        self.chrome.find_element(*self.CONNECT).click()
        self.chrome.find_element(*self.USER).send_keys('irinavoinea@yahoo.com')
        self.chrome.find_element(*self.PAROLA).send_keys('irinairina')
        self.chrome.find_element(*self.CONNECT_BTN).click()
        self.chrome.find_element(*self.MENU_LINK).click()
        self.chrome.find_element(*self.CATEG_ANTISTRES).click()
        self.chrome.find_element(*self.INSOMNIE).click()
        self.chrome.find_element(*self.ALEGE_PROD).click()
        self.chrome.find_element(*self.FAVORITE).click()
        adaugat = 'Valeriana tinctura fara alcool has been added to your Wish List.'
        expected = self.chrome.find_element(*self.MESAJ_FAVORITE).text
        print(expected)
        print('Produs adaugat la Favorite')
        assert adaugat.strip() in expected.strip()
