import configparser

from selenium.webdriver.support.wait import WebDriverWait


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
