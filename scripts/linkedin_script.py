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

path = environ["WEBDRIVER_PATH"]
url = environ["BASE_URL"]
feed_endpoint = environ["FEED_ENDPOINT"]


options = Options()
ua = UserAgent()
user_agent = ua.random

options.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(
    options=options,
    executable_path=path
)


def login_to_linkedin(driver=driver):
    login_uid_xpath = '//*[@id="session_key"]'
    login_password_xpath = '//*[@id="session_password"]'
    login_submit_xpath = '//*[@id="main-content"]/section[1]/div/div/form/button'
    phone_skip_btn = "/html/body/div/div[1]/section/div[2]/div/article/footer/div/div/button"

    try:
        driver.get(url)

        uid_field = driver.find_element(By.XPATH, login_uid_xpath)
        uid_field.send_keys(environ["LINKEDIN_USERNAME"])

        password_field = driver.find_element(By.XPATH, login_password_xpath)
        password_field.send_keys(environ["LINKEDIN_PASSWORD"])

        okay_btn = driver.find_element(By.XPATH, login_submit_xpath)
        okay_btn.click()

        if environ["ADD_PHONE_ENDPOINT"] in driver.current_url:
            btn = driver.find_element(By.XPATH, phone_skip_btn)
            btn.click()
            btn = None
        return driver
    except Exception as e:
        print(e)
        driver.quit()


def scrape():
    driver = login_to_linkedin()
    try:
        driver.get(url + feed_endpoint)
        return driver
    except Exception as e:
        print(e)
        driver.quit()
        exit(1)


def main():
    driver = scrape()
    driver.quit()


if __name__ == "__main__":
    main()
