import configparser

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators.locators import BaseLocators


def get_shop_url():
    config = configparser.ConfigParser()
    config.read("config.ini")
    return config.get("SETUP", "url")


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10, 0.5)
        self.home_url = get_shop_url()

    def open_home_page(self):
        self.driver.get(self.home_url)
        EC.presence_of_element_located(BaseLocators.HOME_PAGE_LOADED)

    def set_newsletter_email(self, email):
        self.driver.find_element(*BaseLocators.NEWSLETTER_INPUT).clear()
        self.driver.find_element(*BaseLocators.NEWSLETTER_INPUT).send_keys(email)

    def join_to_newsletter(self):
        self.driver.find_element(*BaseLocators.NEWSLETTER_SIGN_UP).click()

    def check_error_message_displayed(self, error_message):
        if self.driver.find_element(*BaseLocators.NEWSLETTER_ERROR_MESSAGE).text == error_message:
            return True
        else:
            return False
