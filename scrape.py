import datetime

from selenium.webdriver.common.by import By

from base import openBrowserAndGotoURL, clickButton, SelectAndDownloadFiles
from login import login

driver = openBrowserAndGotoURL('https://www.draftkings.com/lineup/upload')

login(driver, "sonusanglikar54@gmail.com", "Sonu@12345")

SelectAndDownloadFiles(driver,"NBA","CLASSIC")

SelectAndDownloadFiles(driver,"GOLF","SHOWDOWN")

driver.close()
