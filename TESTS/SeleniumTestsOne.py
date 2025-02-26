import time
import unittest
from Utils.SeleniumUtils import SeleniumUtils


class GeeksTest(unittest.TestCase):
    def setUp(self):
        self.target = SeleniumUtils()
        self.target.goto("https://www.geeksforgeeks.org/")

    def test_something(self):
        self.target.enterText({"locator": "xpath", "value": '//*[@id="comp"]/div[2]/div[1]/div[2]/input'}, "gaya")
        time.sleep(1)
        self.target.click(self.target.findBy("xpath",'//*[@id="comp"]/div[2]/div[1]/div[2]/span'))
        self.assertIsNotNone(self.target.driver.title)


if __name__ == '__main__':
    unittest.main()
