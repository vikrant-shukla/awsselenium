import time

from base import waitAndEnterText, clickButton
from initiate_driver import WebDriver
from selenium.webdriver.common.keys import Keys


def login(driver, username, password):
    clickButton(driver, "//div/span[text()='Log In']")
    waitAndEnterText(driver, "//input[@name='username']", username)
    waitAndEnterText(driver, "//input[@name='password']", password)
    clickButton(driver, "//button/span[text()='Log In']")
    time.sleep(5)
