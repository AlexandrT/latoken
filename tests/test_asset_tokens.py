import pytest
import logging

from helpers import page
from helpers.fixtures import test_data


logger = logging.getLogger('ui_site')

REQUEST_PATH = '/tokenization/'

class TestAssetTokens(object):
    """Test asset tokens"""

    def setup_class(cls):
        logger.info('=================================================================')

    def teardown_class(cls):
        logger.info('-----------------------------------------------------------------')

    def setup_method(self, method):
        logger.info('==================TEST STARTED==================')
        logger.info(f"{self.__doc__} {method.__doc__}")

    def teardown_method(self, method):
        logger.info('------------------TEST FINISHED------------------')

    def test_create_ok(self, selenium, main_url):
        """is done"""

        selenium.get(f"{main_url}{REQUEST_PATH}")
        tokenization_page = page.TokenizationPage(selenium)
        tokenization_page.click_assets_token()

        contact_page = page.ContactPage(selenium)
        contact_page.fullName = test_data.FULL_NAME
        contact_page.phone = test_data.PHONE
        contact_page.email = test_data.EMAIL
        contact_page.telegram = test_data.TELEGRAM
        contact_page.click_next_button()

        project_page = page.ProjectPage(selenium)
        project_page.projectName = test_data.PROJECT['NAME']
        project_page.projectDesc = test_data.PROJECT['DESCRIPTION']
        project_page.projectSite = test_data.PROJECT['SITE']
        project_page.click_asset_type()
        project_page.click_first_asset_type()
        project_page.projectIndustry = test_data.PROJECT['INDUSTRY']
        project_page.plan = test_data.PROJECT['PLAN']
        project_page.valuation = test_data.PROJECT['VALUATION']

        project_page.click_submit_button()

        assert(True == True)
