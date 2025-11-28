from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, url=None):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        if self.url:
            self.driver.get(self.url)

    def click(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    def write(self, locator, value):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(value)

    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
