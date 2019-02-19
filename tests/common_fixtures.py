import pytest
import os
from selenium import webdriver

from config import settings

@pytest.fixture
def selenium(selenium, main_url):
    selenium.implicitly_wait(20)
    selenium.get(main_url)
    return selenium

@pytest.fixture
def main_url():
    return settings.DOMAIN

@pytest.fixture
def chrome_options(chrome_options):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')

    return chrome_options
