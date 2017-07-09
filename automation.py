class Automation:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def send_keys_xpath(self, xpath, keys):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, xpath)))
        self.driver.find_element_by_xpath(xpath).send_keys(keys)

    def click_xpath(self, xpath):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, xpath)))
        self.driver.find_element_by_xpath(xpath).click()

    def __del__(self):
        self.driver.close()
