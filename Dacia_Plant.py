from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager import chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import unittest


class Test(unittest.TestCase):
    ACCEPT_BTN = (By.XPATH, '//*[@id="gdprCookieBar"]/div/div[2]/button[2]')
    CONNECT = (By.ID, 'authorization-trigger')
    USER = (By.ID, 'email')
    PAROLA = (By.NAME, 'login[password]')
    CONNECT_BTN = (By.XPATH, '//*[@id="send2"]')
    SELECT = (By.XPATH, '//*[@id="menu-5-65a52e42cc63d"]/ul/li[1]/a')
    CATEG_ANTISTRES = (By.XPATH, "//span[text() = 'Antistres']")
    SORT_PRET = (By.XPATH, '//*[@id="sorter"]/option[4]')
    ERR_MSG = (By.XPATH, "//div[@data-ui-id='message-error']")
    CAUTARE_PROD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, '//*[@id="search_mini_form"]/div[2]/button')
    NR_PROD = (By.XPATH, '// *[ @ id = "category-products-grid"]//li[@class = "item product product-item"]')
    MES_AFISAT = (By.XPATH, '//*[@id="maincontent"]/div[1]/h1/span')
    MENU_LINK = (By.XPATH, "//span[text() = 'La ce folosesc']")
    SELECTIE = (By.XPATH, '//*[@id="narrow-by-list"]/div[1]/div[1]')
    INSOMNIE = (By.XPATH, "//*[text()='Insomnie  ']")
    PRODUSE_INSOMNIE = (By.XPATH, '//*[@id="category-products-grid"]//li[@class = "item product product-item"]')
    ALEGE_PROD = (By.XPATH, '//*[@id="category-products-grid"]/ol/li[2]/div/div[2]/strong/a')
    ADAUGA_COS = (By.ID, 'product-addtocart-button')
    MESAJ_SUCCES = (By.XPATH, '// *[ @ id = "maincontent"] / div[1] / div[2] / div / div / div')
    CLS_ANTISTRES = (By.XPATH,'//*[@id="html-body"]/div[4]/div[1]/div/ul/li[2]/strong')
    COS= (By.XPATH,'//*[@id="html-body"]/div[4]/header/div[2]/div[1]/div/div[3]/div[2]/div[1]/a')
    STERGERE = (By.XPATH,'//*[@id="shopping-cart-table"]/tbody/tr/td[5]/div/a')
    MES_STERGERE = (By.XPATH,'//*[@id="maincontent"]/div[3]/div/div[2]/p[1]')
    DELOGARE_BTN = (By.ID, 'authorization-trigger')
    LOGOUT = (By.XPATH,'//*[@id="cdz-login-form-dropdown"]/div/ul/li[2]/a')
    FAVORITE = (By.XPATH,'//*[@id="product_addtocart_form"]/div[2]/a/span')
    MESAJ_FAVORITE =(By.XPATH,'//*[@id="maincontent"]/div[1]/div[2]/div/div')


    def setUp(self) -> None:
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://www.daciaplant.ro/')

    def tearDown(self) -> None:
        self.chrome.quit()

    def test_check_url(self):
        actual = self.chrome.current_url
        expected = 'https://www.daciaplant.ro/'
        self.assertEqual(actual, expected, 'The page is not correct')
        sleep(2)

    def test_teste1(self):
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
        self.assertEqual(actual, expected, 'contul a fost creat cu succes')
        print('contul a fost creat cu succes')

    def test_teste2(self):
        # verif ca se face ok delogarea din cont
        self.chrome.implicitly_wait(10)
        self.chrome.find_element(*self.ACCEPT_BTN).click()
        self.chrome.find_element(*self.CONNECT).click()
        self.chrome.find_element(*self.USER).send_keys('irinavoinea@yahoo.com')
        self.chrome.find_element(*self.PAROLA).send_keys('irinairina')
        self.chrome.find_element(*self.CONNECT_BTN).click()
        self.chrome.find_element(*self.DELOGARE_BTN).click()
        sleep(1)
        self.chrome.find_element(*self.LOGOUT).click()
        sleep(2)



    def test_teste3(self):
        # se verif ca afiseaza mesaj de err daca se introd parola gresita
        self.chrome.implicitly_wait(10)
        self.chrome.find_element(*self.ACCEPT_BTN).click()
        self.chrome.find_element(*self.CONNECT).click()
        self.chrome.find_element(*self.USER).send_keys('irinavoinea@yahoo.com')
        self.chrome.find_element(*self.PAROLA).send_keys('123456789')
        self.chrome.find_element(*self.CONNECT_BTN).click()
        asteptare_eroare = WebDriverWait(self.chrome, 10).until(EC.presence_of_element_located(self.ERR_MSG))
        if 'The account sign-in' in asteptare_eroare.text:
            print('Mesajul de eroare este afisat')
        else:
            print('mesajul de err nu este afisat')

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

    def test_teste8(self):
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
        print('Produs adaugat in cos')

    def test_teste9(self):
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
        print('produs sters din cos')

    def test_teste10(self):
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
        sleep(1)
        adaugat = 'Valeriana tinctura fara alcool has been added to your Wish List. Faceti click aici pentru a continua cumparaturile.'
        expected = self.chrome.find_element(*self.MESAJ_FAVORITE).text
        assert adaugat in expected
        print('Produs adaugat la Favorite')
