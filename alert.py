from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def alert(driver):
    try:
        WebDriverWait(driver, 1).until(expected_conditions.alert_is_present(), "")
        a = driver.switch_to.alert
        text = a.text
        a.accept()
        return text

    except TimeoutException:
        return False
