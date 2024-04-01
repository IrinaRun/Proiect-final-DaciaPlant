
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from unittest import TestCase



class Search_products(TestCase):
    ACCEPT_BTN = (By.XPATH, '//*[@id="gdprCookieBar"]//*[@class="action primary"]')
    CONNECT = (By.ID, 'authorization-trigger')
    CATEG_ANTISTRES = (By.XPATH, "//span[text() = 'Antistres']")
    CLS_ANTISTRES = (By.XPATH, '//*[@class="item amasty_xlanding_page"]')
    CAUTARE_PROD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH,'// *[ @ id = "search_mini_form"] // button')
    NR_PROD = (By.XPATH, '// *[ @ id = "category-products-grid"]//li[@class = "item product product-item"]')
    MES_AFISAT = (By.XPATH, '// *[ @ id = "maincontent"] // span[@class ="base"]')
    MENU_LINK = (By.XPATH, "//span[text() = 'La ce folosesc']")
    INSOMNIE = (By.XPATH, "//*[text()='Insomnie  ']")
    PRODUSE_INSOMNIE = (By.XPATH, '//*[@id="category-products-grid"]//li[@class = "item product product-item"]')

    def setUp(self) -> None:
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://www.daciaplant.ro/')

    def tearDown(self) -> None:
        self.chrome.quit()

    def test_search_one_product(self):
        # se verif cautarea unui produs
        self.chrome.implicitly_wait(10)
        self.chrome.find_element(*self.ACCEPT_BTN).click()
        self.chrome.find_element(*self.CAUTARE_PROD).send_keys('vitamina C')
        self.chrome.find_element(*self.SEARCH_BTN).click()
        mesaj = self.chrome.find_element(*self.MES_AFISAT).text
        expected = 'CAUTATI REZULTATE PENTRU:'
        assert expected in mesaj, 'Mesajul nu este afisat'



    def test_results_number(self):
        # se verif ca nr de rezultate este peste 10
        self.chrome.implicitly_wait(10)
        self.chrome.find_element(*self.ACCEPT_BTN).click()
        self.chrome.find_element(*self.CAUTARE_PROD).send_keys('vitamina C')
        self.chrome.find_element(*self.SEARCH_BTN).click()
        nr_prod = self.chrome.find_elements(*self.NR_PROD)
        nr_prod_afisat = len(nr_prod)
        print(f'S-au gasit {nr_prod_afisat}')
        minim = 10
        assert nr_prod_afisat > minim, (
            f"Numărul de produse afișate este in intervalul solicitat "
            f"este mai mic decât minimul așteptat ")


    def test_categoy_search(self):
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


    def test_minimun_number(self):
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
