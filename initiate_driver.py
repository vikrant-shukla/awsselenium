try:
    import json
    from selenium.webdriver import Chrome
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.options import Options
    import os
    import shutil
    import uuid
    # import boto3
    from datetime import datetime
    import datetime

    print("All Modules are ok ...")

except Exception as e:

    print("Error in Imports ")



class WebDriver(object):

    def __init__(self):
        self.options = Options()
        self.options.binary_location = '/opt/headless-chromium'
        self.options.add_argument('--headless')
        self.options.add_argument('--no-sandbox')
        self.options.add_argument("--start-maximized")
        self.options.add_argument('--start-fullscreen')
        self.options.add_argument('--single-process')
        self.options.add_argument('--disable-dev-shm-usage')

    def get(self):
        # driver = Chrome('/opt/chromedriver', options=self.options)
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        return driver


