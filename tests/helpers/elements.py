from selenium.webdriver.support.ui import WebDriverWait

from .locators import *


class PageElement(object):
    def __set__(self, obj, value):
        driver = obj.driver
        WebDriverWait(driver, 100).until(lambda driver:
                driver.find_element(*self.locator))

        driver.find_element(*self.locator).send_keys(value)

    def __get__(self, obj, owner):
        driver = obj.driver
        item = driver.find_element(*self.locator)
        element = item.find_element(*ContactPageLocators.WRAPPER)

        return element.get_attribute("class")
