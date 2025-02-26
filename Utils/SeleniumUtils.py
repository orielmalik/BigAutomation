import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement


from Utils.Logger import printer


class SeleniumUtils:
    def __init__(self, browser='edge'):
        if browser.lower() == "chrome":
            self.driver = webdriver.Chrome()
        else:
            self.driver = webdriver.Edge()

    def quit(self):
        printer("info", "Quitting SeleniumUtils")
        self.driver.quit()

    def goto(self, url):
        printer("info", f"goto {url}")
        self.driver.get(url)

    def findBy(self, category, val):
        res = self.by_locator(str(category).upper())
        try:
            printer("debug", f"Trying to find element by {category}: {val}")
            return self.driver.find_element(res, val)
        except NoSuchElementException:
            printer("error", f"Element not found by {category}: {val}")
            return None

    def click(self, element):
        if element:
            printer("debug", f"Clicked on element: {element.tag_name}")
            element.click()
        else:
            printer("error", "Element not found to click!")

    def sendKeys(self, element, value):
        if isinstance(element, WebElement):
            element.send_keys(value)
        else:
            printer("error", f"❌ Error: The provided element is not a valid WebElement!")
            raise TypeError("The element is not a WebElement!")

    def enterText(self, dictSend, value):
        if not isinstance(dictSend, dict):
            printer("error", "The provided input is not a dictionary!")
            raise TypeError("Expected a dictionary as input.")

        if "locator" in dictSend and "value" in dictSend:
            element = self.findBy(dictSend["locator"], dictSend["value"])
            if element:
                self.sendKeys(element, value)
            else:
                printer("error", f"Element not found for {dictSend['locator']} with value {dictSend['value']}")
        else:
            printer("error", "Missing 'locator' or 'value' in the input dictionary.")
            raise KeyError("Missing required keys in dictionary: 'locator' or 'value'")

    def by_locator(self, locator_type: str):
        mapping = {
            "ID": By.ID,
            "XPATH": By.XPATH,
            "LINK_TEXT": By.LINK_TEXT,
            "PARTIAL_LINK_TEXT": By.PARTIAL_LINK_TEXT,
            "NAME": By.NAME,
            "TAG_NAME": By.TAG_NAME,
            "CLASS_NAME": By.CLASS_NAME,
            "CSS_SELECTOR": By.CSS_SELECTOR,
        }
        try:
            return mapping[locator_type.upper()]
        except KeyError:
            printer("error", f"❌ Invalid locator type: {locator_type}")
            raise ValueError(f"Invalid locator type: {locator_type}")

    def upload_file(driver, locator, file_path):
        element = driver.find_element(By.XPATH, locator)
        element.send_keys(file_path)

    def take_screenshot(driver, filename):
        driver.save_screenshot(filename)
