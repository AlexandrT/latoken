from selenium.webdriver.common.by import By


class TokenizationPageLocators(object):
    ASSET_TOKENS_BLOCK = (By.XPATH, '//div[contains(@class, \
    "tokenizationType")]/img[contains(@src, "asset_token")]')

class ContactPageLocators(object):
    FULL_NAME_INPUT = (By.ID, 'wizard-asset-tokens-your-full-name')
    PHONE_INPUT = (By.ID, 'wizard-asset-tokens-mobile-phone')
    EMAIL_INPUT = (By.ID, 'wizard-asset-tokens-email')
    TELEGRAM_INPUT = (By.ID, 'wizard-asset-tokens-telegram-contact')

    WRAPPER = (By.XPATH, './ancestor::div[contains(@class, "ant-form-item-control") and not(contains(@class, "wrapper"))]')

    NEXT_BUTTON = (By.ID, 'next')

class ProjectPageLocators(object):
    PROJECT_NAME_INPUT = (By.ID, 'wizard-asset-tokens-project-name')
    PROJECT_DESC_AREA = (By.ID, 'wizard-asset-tokens-project-description')
    PROJECT_SITE_INPUT = (By.ID, 'wizard-asset-tokens-project-website')
    ASSET_TYPE_INPUT = (By.ID, 'wizard-asset-tokens-asset-type')
    ASSET_TYPE_ITEMS = (By.XPATH, '//li[@role="option"]')
    PROJECT_INDUSTRY_INPUT = (By.ID, 'wizard-asset-tokens-project-industry')
    PLAN_AREA = (By.ID, 'wizard-asset-tokens-plan-to-use')
    VALUATION_INPUT = (By.ID, 'wizard-asset-tokens-asset-token-valuation')

    SUBMIT_BUTTON = (By.ID, 'submit-request')
