import unittest
from selenium import webdriver


class OnionExplorerTest(unittest.TestCase):
    '''
    based on https://engineering.aweber.com/getting-started-with-ui-automated-tests-using-selenium-python/
    '''

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()

    def test_title(self):
        self.driver.get('http://127.0.0.1:8081/')
        self.assertEqual(
            self.driver.title,
            'Onion Monero Blockchain Explorer')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()