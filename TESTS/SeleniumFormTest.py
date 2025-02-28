import os
import time
import unittest
import json
from Utils.SeleniumUtils import SeleniumUtils
from pathlib import Path


def reaData():
    project_root = Path(__file__).resolve().parent.parent

    json_file = project_root / "JSONS" / "Jones.json"
    with json_file.open("r", encoding="utf-8") as file:
        return json.load(file)


class SeleniumFormTest(unittest.TestCase):
    def setUp(self):
        self.driver = SeleniumUtils()
        self.data = reaData()
        self.driver.goto("https://testsite.getjones.com/ExampleForm/")

    def test_forms(self):
        for i in range(len(self.data)):
            for key, value in self.data[i].items():
                self.driver.enterText({"locator": "name", "value": key}, value)
            self.driver.click(self.driver.findBy("xpath", "/html/body/div/div[2]/div[2]/div/form/p[6]/button"))
            time.sleep(1)
            assert str(self.driver.getTitle()) == "ExampleForm"
