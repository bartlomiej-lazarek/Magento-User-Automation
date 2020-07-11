from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as ec

from locators.locators import HomeLocators, ProductLocators
from pages.base_page import BasePage


class HomePage(BasePage):

    def open_home_page(self):
        self.driver.get(self.home_url)
        self.wait.until(ec.presence_of_element_located(HomeLocators.HOME_PAGE_LOADED))

    def set_newsletter_email(self, email):
        self.driver.find_element(*HomeLocators.NEWSLETTER_INPUT).clear()
        self.driver.find_element(*HomeLocators.NEWSLETTER_INPUT).send_keys(email)

    def join_to_newsletter(self):
        self.driver.find_element(*HomeLocators.NEWSLETTER_SIGN_UP).click()

    def check_error_message_displayed(self, error_message):
        return self.driver.find_element(*HomeLocators.NEWSLETTER_ERROR_MESSAGE).text == error_message

    def go_to_authentication_page(self):
        self.driver.find_element(*HomeLocators.MY_ACCOUNT_ICON).click()

    def hover_on_first_product(self):
        ActionChains(self.driver).move_to_element(
            self.driver.find_element(*HomeLocators.PRODUCT_IMAGE)).perform()

    def click_on_first_product(self):
        self.driver.find_element(*HomeLocators.PRODUCT_IMAGE).click()

    def add_to_wish_list(self):
        self.driver.find_element(*HomeLocators.ADD_TO_WISH_LIST_BUTTON).click()

    def add_to_cart(self):
        self.driver.find_element(*HomeLocators.ADD_TO_CART_BUTTON).click()

    def go_to_page_with_configurable_product_on_list(self):
        self.driver.get(self.list_view_configurable_options)
        self.wait.until(ec.presence_of_element_located(HomeLocators.HOME_PAGE_LOADED))

    def go_to_configurable_product_page(self):
        self.driver.get(self.configurable_product_page)
        self.wait.until(ec.presence_of_element_located(HomeLocators.HOME_PAGE_LOADED))

    def choose_first_attribute(self):
        self.driver.find_element(*ProductLocators.PRODUCT_OPTIONS).click()
