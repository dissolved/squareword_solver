from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Driver:
    def __init__(self):
        self.driver = None

    def __enter__(self):
        self.driver = webdriver.Firefox()

        # load the puzzle
        self.driver.get("https://squareword.org/")

        # dismiss instructions
        element = self.driver.switch_to.active_element
        element.send_keys(Keys.ESCAPE)
        return self

    def __exit__(self, _exc_type, _exc_value, _exc_tb):
        self.driver.close()

    def submit_guess(self, guess):
        element = self.driver.switch_to.active_element
        element.send_keys(guess + Keys.RETURN)
