import unittest
from selenium import webdriver


class OnionExplorerTest(unittest.TestCase):
    '''
    based on https://engineering.aweber.com/getting-started-with-ui-automated-tests-using-selenium-python/
    '''

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.url = 'http://127.0.0.1:8081/'

    def test_title(self):
        self.driver.get(self.url)
        self.assertEqual(self.driver.title, 'Onion Monero Blockchain Explorer')

    def test_footer(self):
         self.driver.get(self.url)
         self.assertIn('source code', self.driver.page_source)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()