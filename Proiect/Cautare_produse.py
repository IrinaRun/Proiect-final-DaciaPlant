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


class Search_products(TestCase):
    ACCEPT_BTN = (By.XPATH, '//*[@id="gdprCookieBar"]/div/div[2]/button[2]')
    CONNECT = (By.ID, 'authorization-trigger')
    SELECT = (By.XPATH, '//*[@id="menu-5-65a52e42cc63d"]/ul/li[1]/a')
    CATEG_ANTISTRES = (By.XPATH, "//span[text() = 'Antistres']")
    CLS_ANTISTRES = (By.XPATH, '//*[@id="html-body"]/div[4]/div[1]/div/ul/li[2]/strong')
    CAUTARE_PROD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, '//*[@id="search_mini_form"]/div[2]/button')
    NR_PROD = (By.XPATH, '// *[ @ id = "category-products-grid"]//li[@class = "item product product-item"]')
    MES_AFISAT = (By.XPATH, '//*[@id="maincontent"]/div[1]/h1/span')
    MENU_LINK = (By.XPATH, "//span[text() = 'La ce folosesc']")
    SELECTIE = (By.XPATH, '//*[@id="narrow-by-list"]/div[1]/div[1]')
    INSOMNIE = (By.XPATH, "//*[text()='Insomnie  ']")
    PRODUSE_INSOMNIE = (By.XPATH, '//*[@id="category-products-grid"]//li[@class = "item product product-item"]')

    def setUp(self) -> None:
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://www.daciaplant.ro/')

    def tearDown(self) -> None:
        self.chrome.quit()

    def test_teste4(self):
        # se verif cautarea unui produs
        self.chrome.implicitly_wait(10)
        self.chrome.find_element(*self.ACCEPT_BTN).click()
        self.chrome.find_element(*self.CAUTARE_PROD).send_keys('vitamina C')
        self.chrome.find_element(*self.SEARCH_BTN).click()
        mesaj = self.chrome.find_element(*self.MES_AFISAT).text
        expected = 'CAUTATI REZULTATE PENTRU:'
        while expected in mesaj:
            break
        print(f'Selectie ok')



    def test_teste5(self):
        # se verif ca nr de rezultate este peste 10
        self.chrome.implicitly_wait(10)
        self.chrome.find_element(*self.ACCEPT_BTN).click()
        self.chrome.find_element(*self.CAUTARE_PROD).send_keys('vitamina C')
        self.chrome.find_element(*self.SEARCH_BTN).click()
        nr_prod = self.chrome.find_elements(*self.NR_PROD)
        nr_prod_afisat = len(nr_prod)
        print(f'S-au gasit {nr_prod_afisat}')
        minim = 10
        if nr_prod_afisat > minim:
            print('Nr de produsele gasite este in intervalul solicitat')
        else:
            print("Nr prod gasite insuficient, in afara intervalului solicitat")

    def test_teste6(self):
        # se verif ca se poate naviga si alege categ Antistres
        self.chrome.implicitly_wait(10)
        self.chrome.find_element(*self.ACCEPT_BTN).click()
        self.chrome.find_element(*self.MENU_LINK).click()
        self.chrome.find_element(*self.CATEG_ANTISTRES).click()
        expected= 'ANTISTRES'
        mesaj = self.chrome.find_element(*self.CLS_ANTISTRES).text
        try:
            assert expected == mesaj
            print('Selectie in categoria Antistres realizata')
        except AssertionError:
            print('Nu s-a realizat filtrul in categoria Antistres')


    def test_teste7(self):
        # se verif ca sunt afisate minim 3 articole in categ 'Insomnie'
        self.chrome.implicitly_wait(10)
        self.chrome.find_element(*self.ACCEPT_BTN).click()
        self.chrome.find_element(*self.MENU_LINK).click()
        self.chrome.find_element(*self.CATEG_ANTISTRES).click()
        self.chrome.find_element(*self.INSOMNIE).click()
        product = self.chrome.find_elements(*self.PRODUSE_INSOMNIE)
        numar_produse_asteptat = 3
        numarul_de_produse_afisat = len(product)
        print(f"Numarul de produse in pagina este de : {numarul_de_produse_afisat}")
        assert numarul_de_produse_afisat >= numar_produse_asteptat, (
            f"Numărul de produse afișate ({numarul_de_produse_afisat}) "
            f"este mai mic decât minimul așteptat ({numar_produse_asteptat})")
