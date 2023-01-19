import os

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.common.action_chains import ActionChains


class ToneGeneratorBot:
    def __init__(self, driver=None):
        self._playing = False
        self._website_url = os.environ.get('WEBSITE_URL')
        if driver:
            self._driver = driver
        else:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_experimental_option("excludeSwitches",
                                ['enable-automation', 'enable-logging'])
            chrome_options.headless = True
            chromedriver_path = os.environ.get('CHROMEDRIVER_PATH')
            service = Service(chromedriver_path)
            self._driver = webdriver.Chrome(service=service, 
                                        options=chrome_options)

    def execute(self):
        if self._playing:
            print("press 1 to exit, press 2 to stop sound\npress any other key to continue")
        else:
            print("press 1 to exit, press any other key to continue")
        x = input()
        if x == '1':
            return
        if x == '2' and self._playing:
            self._driver.find_element(By.ID, 'play-button').click()
            self._playing = False
            self.execute()
            return
        print("Enter a frequency between 1 and 20,154 Hz (will be rounded to 3 decimal places)")
        f = float(input())
        print("Enter an integer amplitude between 0 and 100%")
        a = int(round(float(input())))
        self._driver.get(f'{self._website_url}/tone#{f},v0.{a}')
        self._driver.find_element(By.ID, 'play-button').click()
        self._playing = True
        self.execute()


if __name__ == '__main__':
    load_dotenv()
    bot = ToneGeneratorBot()
    bot.execute()
