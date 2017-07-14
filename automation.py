import os
import shutil
import sys
import zipfile

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Automation:
    def __init__(self):
        if not os.path.isfile("chromedriver.exe"):
            print("chromedriver.exe가 존재하지 않습니다. 최신 릴리즈를 최초 1회 다운로드합니다.", file=sys.stderr)

            chromedriver_latest_release = requests.get(
                "https://chromedriver.storage.googleapis.com/LATEST_RELEASE").text.strip()

            r = requests.get("https://chromedriver.storage.googleapis.com/"
                             + chromedriver_latest_release + "/chromedriver_win32.zip", stream=True)

            with open("chromedriver_win32.zip", "wb") as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)

            with zipfile.ZipFile("chromedriver_win32.zip") as zip:
                zip.extract("chromedriver.exe")

            os.remove("chromedriver_win32.zip")

        self.driver = webdriver.Chrome()

    def __del__(self):
        self.driver.quit()

    def send_keys_xpath(self, xpath, keys):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, xpath)))
        x = self.driver.find_element_by_xpath(xpath)
        x.clear()
        x.click()
        x.send_keys(Keys.TAB)
        x.send_keys(keys)

    def click_css_selector(self, css_selector, wait=10):
        WebDriverWait(self.driver, wait).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))
        self.driver.find_element_by_css_selector(css_selector).click()

    def find_css_selector(self, css_selector, wait=10):
        WebDriverWait(self.driver, wait).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))
        return self.driver.find_element_by_css_selector(css_selector)

    def click_xpath(self, xpath, wait=10):
        WebDriverWait(self.driver, wait).until(expected_conditions.element_to_be_clickable((By.XPATH, xpath)))
        self.driver.find_element_by_xpath(xpath).click()

    def find_xpath(self, xpath, wait=10):
        WebDriverWait(self.driver, wait).until(expected_conditions.element_to_be_clickable((By.XPATH, xpath)))
        return self.driver.find_element_by_xpath(xpath)

    @staticmethod
    def read_txt(filename, sep=None):
        with open(filename, "r") as f:
            for l in f:
                if sep is not None:
                    yield l.strip().split(sep)
                else:
                    yield l.strip()


def main():
    a = Automation()

main()
