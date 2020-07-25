import configparser

from selenium.webdriver.support.wait import WebDriverWait

from locators.locators import HomeLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10, 0.5)
        self.config = configparser.ConfigParser()
        self.config.read("config.ini")
        self.home_url = self.config.get("SETUP", "url_page")
        self.list_view_configurable_options = self.config.get(
            "SETUP", "url_list_view_configurable_options")
        self.configurable_product_page = self.config.get(
            "SETUP", "url_configurable_product_page")

    @staticmethod
    def string_to_float_price(price):
        return float(price.split(" ")[0].replace(",", "."))

    def check_if_success_msg_displayed(self):
        return len(self.driver.find_elements(*HomeLocators.SUCCESS_MESSAGE)) > 0

    def check_if_error_msg_displayed(self):
        return len(self.driver.find_elements(*HomeLocators.ERROR_MESSAGE)) > 0
