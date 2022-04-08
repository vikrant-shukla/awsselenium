import random
import time
from datetime import datetime

from selenium.webdriver.common.by import By

from initiate_driver import WebDriver
from selenium.webdriver.common.keys import Keys


def openBrowserAndGotoURL(url):
    instance_ = WebDriver()
    driver = instance_.get()
    driver.implicitly_wait(10)
    driver.get(url)
    return driver


def waitAndEnterText(driver, xpath, text):
    field = driver.find_element_by_xpath(xpath)
    field.send_keys(text)
    time.sleep(5)


def clickButton(driver, xpath):
    field = driver.find_element_by_xpath(xpath)
    field.click()
    time.sleep(5)


def SelectAndDownloadFiles(driver, textToBeClickForSlot, textToBeClickForSport):
    '''Select SLot'''
    time.sleep(10)
    clickButton(driver, "(//h3[text()='Pick a Sport']/../div/a)[1]")
    clickButton(driver, f"//li/a[text()='{textToBeClickForSlot}']")

    '''Select Style'''
    clickButton(driver, "(//h3[text()='Pick a Sport']/../div/a)[2]")
    clickButton(driver, f"//li/a[text()='{textToBeClickForSport}']")

    '''Selecting start time'''
    links = []
    elemets = driver.find_elements(By.XPATH, "//h3[text()='Pick a Start Time']/../ul/li")
    print(elemets)
    for i in elemets:
        print(i)
        i.find_element(By.XPATH, ".//a").click()
        links.append(driver.find_element(By.XPATH, "//a[text()=' DOWNLOAD']").get_attribute("href"))

    '''Dowmload file '''
    import requests
    for link in links:
        req = requests.get(link, allow_redirects=True)

        open("file" + str(random.randint(0, 99999999999)) + ".csv", 'wb').write(req.content)
