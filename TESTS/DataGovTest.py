import time
import unittest
from Utils.SeleniumUtils import SeleniumUtils
from Utils.CONSTANS import *


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = SeleniumUtils(chrome);

    def test_beforeSearch(self):
        self.driver.goto(GOV_IL).findAndDo("click", "xpath", '//*[@id="carouselContentControls-0"]/div[2]/a')
        self.assertTrue(str(self.driver.get("url")) != GOV_IL, str(self.driver.get("url")))


if __name__ == '__main__':
    unittest.main()
