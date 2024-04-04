import unittest

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

        # report_path = 'test_report.html'
        report_path = 'Test_Report.txt'
        with open(report_path, 'w') as report_file:
            runner = HTMLTestRunner(combine_reports=True, report_title = "Test execution report",
                report_name = "Test results" )
            runner.run(teste_de_rulat)



