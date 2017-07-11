from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Automation:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def __del__(self):
        self.driver.close()

    def send_keys_xpath(self, xpath, keys):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, xpath)))
        x = self.driver.find_element_by_xpath(xpath)
        x.clear()
        x.click()
        x.send_keys(Keys.TAB)
        x.send_keys(keys)

    def click_xpath(self, xpath):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, xpath)))
        self.driver.find_element_by_xpath(xpath).click()

    def find_xpath(self, xpath):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, xpath)))
        return self.driver.find_element_by_xpath(xpath)

    @staticmethod
    def read_txt(filename, sep=None):
        with open(filename, "r") as f:
            for l in f:
                if sep is not None:
                    yield l.strip().split(sep)
                else:
                    yield l.strip()

