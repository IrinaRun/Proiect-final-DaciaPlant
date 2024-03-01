import unittest

# from HtmlTestRunner.runner import HTMLTestRunner
import HTMLTestRunner
from HTMLTestRunner.runner import HTMLTestRunner

from Proiect.Conectare import Login
from Proiect.Cautare_produse import Search_products
from Proiect.Adaugare_produse import Add_to_cart


class TestSuite(unittest.TestCase):

    def test_suite(self):
        teste_de_rulat = unittest.TestSuite()
        teste_de_rulat.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Login),
            unittest.defaultTestLoader.loadTestsFromTestCase(Search_products),
            unittest.defaultTestLoader.loadTestsFromTestCase(Add_to_cart)
        ])

        # runner = HTMLTestRunner(log=True, )
        # runner.run(teste_de_rulat)

        with open('test_report.text', 'w') as f:
            runner = unittest.TextTestRunner(f, verbosity=2)
            runner.run(teste_de_rulat)
