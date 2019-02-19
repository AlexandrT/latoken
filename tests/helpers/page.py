from .locators import *
from .elements import *


class FullName(PageElement):
    locator = ContactPageLocators.FULL_NAME_INPUT

class Phone(PageElement):
    locator = ContactPageLocators.PHONE_INPUT

class Email(PageElement):
    locator = ContactPageLocators.EMAIL_INPUT

class Telegram(PageElement):
    locator = ContactPageLocators.TELEGRAM_INPUT

class ProjectName(PageElement):
    locator = ProjectPageLocators.PROJECT_NAME_INPUT

class ProjectDesc(PageElement):
    locator = ProjectPageLocators.PROJECT_DESC_AREA

class ProjectSite(PageElement):
    locator = ProjectPageLocators.PROJECT_SITE_INPUT

class ProjectIndustry(PageElement):
    locator = ProjectPageLocators.PROJECT_INDUSTRY_INPUT

class Plan(PageElement):
    locator = ProjectPageLocators.PLAN_AREA

class Valuation(PageElement):
    locator = ProjectPageLocators.VALUATION_INPUT

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class TokenizationPage(BasePage):
    def click_assets_token(self):
        element = self.driver.find_element(
                *TokenizationPageLocators.ASSET_TOKENS_BLOCK)
        element.click()

class ContactPage(BasePage):
    fullName = FullName()
    phone    = Phone()
    email    = Email()
    telegram = Telegram()

    def click_next_button(self):
        element = self.driver.find_element(*ContactPageLocators.NEXT_BUTTON)
        element.click()

class ProjectPage(BasePage):
    projectName     = ProjectName()
    projectDesc     = ProjectDesc()
    projectSite     = ProjectSite()
    projectIndustry = ProjectIndustry()
    plan            = Plan()
    valuation       = Valuation()

    def click_asset_type(self):
        element = self.driver.find_element(*ProjectPageLocators.ASSET_TYPE_INPUT)
        element.click()

    def get_asset_type_items(self):
        elements = \
            self.driver.find_elements(*ProjectPageLocators.ASSET_TYPE_ITEMS)
        return elements

    def click_first_asset_type(self):
        elements = self.get_asset_type_items()
        elements[0].click()

    def click_submit_button(self):
        element = self.driver.find_element(*ProjectPageLocators.SUBMIT_BUTTON)
        element.click()
