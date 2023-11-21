from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import sys

class MyBot:
    def __init__(self):
        try:
            user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"

            self.options = webdriver.ChromeOptions()
            self.options.headless = True
            self.options.add_argument(f'user-agent={user_agent}')
            self.options.add_argument("--window-size=1920,1080")
            self.options.add_argument('--ignore-certificate-errors')
            self.options.add_argument('--allow-running-insecure-content')
            self.options.add_argument("--disable-extensions")
            self.options.add_argument("--proxy-server='direct://'")
            self.options.add_argument("--proxy-bypass-list=*")
            self.options.add_argument("--start-maximized")
            self.options.add_argument('--disable-gpu')
            self.options.add_argument('--disable-dev-shm-usage')
            self.options.add_argument('--no-sandbox')
            self.options.add_argument("--headless")

            # Use the Service class to set the executable path
            chrome_path = "drivers/chromedriver.exe"
            self.service = ChromeService(chrome_path)
            
            # Redirect stderr to a file to suppress GPU-related errors
            sys.stderr = open("error_log.txt", "w")
            
            self.driver = webdriver.Chrome(service=self.service, options=self.options)

            self.driver.get("https://yo.fan/cosmo")
            print("Chrome version:", self.driver.capabilities['browserVersion'])
            print(self.driver.title)

            # Add sleep for 3 seconds
            sleep(3)

            # Scroll down the page
            self.scroll_down()

            # Add sleep for 3 seconds
            sleep(3)

            # Scroll up the page
            self.scroll_up()

            # Capture a screenshot after scrolling actions
            self.driver.get_screenshot_as_file("screenshot.png")

        except WebDriverException as e:
            print(f"An error occurred: {e}")

        finally:
            # Close the WebDriver, whether an exception occurred or not
            self.driver.quit()
            # Restore stderr
            sys.stderr.close()

    def scroll_down(self):
        # Scroll down using ActionChains
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.PAGE_DOWN)
        actions.perform()

    def scroll_up(self):
        # Scroll up using ActionChains
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.PAGE_UP)
        actions.perform()

# Create an instance of the MyBot class
MyBot()
