from Provider.driverProvider import *
from page import AutomationTest
import unittest
import warnings

class TestPythonPageSearch(unittest.TestCase):

    def setUp(self):
        self.driver = Provider.seleniumdriver("kaytari")
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

    def test_search_python_page(self):
        #Action
        AutomationTest.run(self.driver, "https://www.python.org", "q", "println")
        #Asset
        self.assertTrue("println" in self.driver.page_source)

    def test_search_ebay_page(self):
        #Action
        AutomationTest.run(self.driver, "https://www.ebay.co.uk/", "_nkw", "Laptop")
        #Asset
        self.assertTrue("Lenovo" in self.driver.page_source)

    def test_click_button_python_page(self):
        #Action
        AutomationTest.runandclick(self.driver, "https://www.python.org", "donate-button")
        #Asset
        self.assertTrue("Donation for the PSF" in self.driver.page_source)    

    def tearUp(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()

