import json
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.remote.webelement import WebElement

from Utils.Logger import printer
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SeleniumUtils:
    def __init__(self, browser='edge'):
        """
        Initializes the Selenium WebDriver.
        :param browser: Specifies which browser to use ('chrome' or 'edge'). Default is 'edge'.
        """
        if browser.lower() == "chrome":
            self.driver = webdriver.Chrome()
        else:
            self.driver = webdriver.Edge()

    def quit(self):
        """
        Quits the WebDriver and closes all associated browser windows.
        """
        printer("info", "Quitting SeleniumUtils")
        self.driver.quit()

    def goto(self, url):
        """
        Navigates the browser to the specified URL.
        :param url: The URL to visit.
        :return: Returns the instance of SeleniumUtils.
        """
        printer("info", f"goto {url}")
        self.driver.get(url)
        return self

    def findBy(self, category, val):
        """
        Finds an element on the page using a specified locator strategy.
        :param category: The type of locator (e.g., 'ID', 'XPATH', 'CSS_SELECTOR').
        :param val: The actual locator value.
        :return: The found WebElement or None if not found.
        """
        res = self.by_locator(str(category).upper())
        try:
            printer("debug", f"Trying to find element by {category}: {val}")
            return self.driver.find_element(res, val)
        except NoSuchElementException:
            printer("error", f"Element not found by {category}: {val}")
            return None

    def click(self, element):
        """
        Clicks on a WebElement if it exists.
        :param element: The WebElement to click.
        """
        if element:
            printer("debug", f"Clicked on element: {element.tag_name}")
            element.click()
            self.wait_for_page_load(10)
        else:
            printer("error", "Element not found to click!")

    def sendKeys(self, element, value):
        """
        Sends keystrokes to an input field.
        :param element: The target WebElement.
        :param value: The text to input.
        :raises TypeError: If the provided element is not a WebElement.
        """
        if isinstance(element, WebElement):
            element.send_keys(value)
        else:
            printer("error", f"❌ Error: The provided element is not a valid WebElement!")
            raise TypeError("The element is not a WebElement!")

    def get(self, opt="title"):
        """
        Retrieves information from the WebDriver.
        :param opt: The option to retrieve ('title' for page title, 'url' for current URL).
        :return: The page title or current URL.
        """
        if opt == "url":
            return self.driver.current_url
        return self.driver.title

    def wait_for_page_load(self, timeout=10):
        """
        Waits for the page to load by checking the current URL or the presence of an element.

        :param timeout: The maximum number of seconds to wait (default is 10)
        :return: None
        """
        try:
            # Save the current URL
            current_url = self.driver.current_url

            # Wait until the URL changes (indicating the page has loaded)
            WebDriverWait(self.driver, timeout).until(EC.url_changes(current_url))

            printer("debug", "Page loaded successfully.")

        except TimeoutException:
            printer("error", f"Timed out waiting for the page to load within {timeout} seconds.")
    def wait_for_element(self, locator, timeout=10):
        """
        Waits for an element to be present on the page.

        :param locator: The locator of the element (e.g., By.ID, By.XPATH, etc.)
        :param timeout: The maximum number of seconds to wait (default is 10)
        :return: The WebElement if found within the time limit, else None
        """
        try:
            # Wait until the element is visible within the timeout period
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return element
        except TimeoutException:
            printer("error", f"Element with locator {locator} was not found within {timeout} seconds.")
            return None

    def enterText(self, dictSend, value):
        """
        Finds an input field and enters text.
        :param dictSend: A dictionary with 'locator' and 'value' keys to identify the element.
        :param value: The text to enter.
        :raises TypeError: If dictSend is not a dictionary.
        :raises KeyError: If required keys are missing.
        """
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
        """
        Maps a string locator type to Selenium's By class.
        :param locator_type: The type of locator (e.g., 'ID', 'XPATH', 'CLASS_NAME').
        :return: The corresponding By value.
        :raises ValueError: If the locator type is invalid.
        """
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

    def findAndDo(self, opt, category, locator, value=''):
        """
        Finds an element and performs an action.
        :param opt: The action to perform ('click' for clicking).
        :param category: The type of locator (e.g., 'ID', 'XPATH').
        :param locator: The locator value.
        :param value: Optional value for input fields (unused here).
        :return: Returns the instance of SeleniumUtils.
        """
        founder = self.findBy(category, locator)
        time.sleep(1)
        if opt == "click":
            self.click(founder)
            return self



    def take_screenshot(driver, filename):
        """
        Takes a screenshot of the current browser window.
        :param driver: The WebDriver instance.
        :param filename: The name of the file to save the screenshot.
        """
        driver.save_screenshot(filename)
