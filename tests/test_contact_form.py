import pytest
import logging

from helpers import page
from helpers.fixtures import test_data


logger = logging.getLogger('ui_site')

REQUEST_PATH = '/tokenization/'

class TestContactForm(object):
    """Test contact form"""

    def setup_class(cls):
        logger.info('=================================================================')

    def teardown_class(cls):
        logger.info('-----------------------------------------------------------------')

    def setup_method(self, method):
        logger.info('==================TEST STARTED==================')
        logger.info(f"{self.__doc__} {method.__doc__}")

    def teardown_method(self, method):
        logger.info('------------------TEST FINISHED------------------')

    def test_empty(self, selenium, main_url):
        """fullName, email, phone are empty"""

        selenium.get(f"{main_url}{REQUEST_PATH}")
        tokenization_page = page.TokenizationPage(selenium)
        tokenization_page.click_assets_token()

        contact_page = page.ContactPage(selenium)
        assert(test_data.CLASS_ERROR not in contact_page.fullName)
        assert(test_data.CLASS_ERROR not in contact_page.phone)
        assert(test_data.CLASS_ERROR not in contact_page.email)
        assert(test_data.CLASS_ERROR not in contact_page.telegram)

        contact_page.telegram = test_data.TELEGRAM

        contact_page.click_next_button()

        assert(test_data.CLASS_ERROR in contact_page.fullName)
        assert(test_data.CLASS_ERROR in contact_page.phone)
        assert(test_data.CLASS_ERROR in contact_page.email)
        assert(test_data.CLASS_ERROR not in contact_page.telegram)

