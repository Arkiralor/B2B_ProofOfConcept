from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType
import requests
from dotenv import load_dotenv
from os import environ
import random
import pandas as pd
import time
from fake_useragent import UserAgent

load_dotenv()
random.seed()

class LinkedinScraper:

    path = environ["WEBDRIVER_PATH"]
    url = environ["BASE_URL"]
    feed_endpoint = environ["FEED_ENDPOINT"]
    search_endpoint = environ["SEARCH_ENDPOINT"]
    search_ender = environ["SEARCH_ENDPOINT_ENDER"]


    options = Options()
    ua = UserAgent()
    user_agent = ua.random

    options.add_argument(f'user-agent={user_agent}')
    driver = webdriver.Chrome(
        options=options,
        executable_path=path
    )

    @classmethod
    def login_to_linkedin(cls):
        '''
        Method to login to linkedin via the driver
        '''
        login_uid_xpath = '//*[@id="session_key"]'
        login_password_xpath = '//*[@id="session_password"]'
        login_submit_xpath = '//*[@id="main-content"]/section[1]/div/div/form/button'
        phone_skip_btn = "/html/body/div/div[1]/section/div[2]/div/article/footer/div/div/button"

        try:
            cls.driver.get(cls.url)

            uid_field = cls.driver.find_element(By.XPATH, login_uid_xpath)
            uid_field.send_keys(environ["LINKEDIN_USERNAME"])

            password_field = cls.driver.find_element(By.XPATH, login_password_xpath)
            password_field.send_keys(environ["LINKEDIN_PASSWORD"])

            okay_btn = cls.driver.find_element(By.XPATH, login_submit_xpath)
            okay_btn.click()

            if environ["ADD_PHONE_ENDPOINT"] in cls.driver.current_url:
                btn = cls.driver.find_element(By.XPATH, phone_skip_btn)
                btn.click()
                btn = None
        except Exception as e:
            print(e)
            cls.driver.quit()

    @classmethod
    def get_feed(cls, feed_type, page_num):
        try:
            cls.driver.get(cls.url + cls.feed_endpoint)

        except Exception as e:
            print(e)
            cls.driver.quit()


    def scrape(cls):
        cls.login_to_linkedin()
        try:
            cls.driver.get(cls.url)
        except Exception as e:
            print(e)
            cls.driver.quit()
            exit(1)


def main():
    LinkedinScraper.scrape()
    LinkedinScraper.driver.quit()


if __name__ == "__main__":
    main()
