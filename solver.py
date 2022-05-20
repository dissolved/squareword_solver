import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def setup(driver):
    # load the puzzle
    driver.get("https://squareword.org/")

    # dismiss instructions
    element = driver.switch_to.active_element
    element.send_keys(Keys.ESCAPE)

def submit_guess(driver, guess):
    element = driver.switch_to.active_element
    element.send_keys(guess + Keys.RETURN)

def main():
    with webdriver.Firefox() as driver:
        setup(driver)
        submit_guess(driver, "moist")
        time.sleep(5)

if __name__ == '__main__':
    main()
