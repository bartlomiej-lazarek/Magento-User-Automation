from locators.locators import RegistrationLocators
from pages.base_page import BasePage


class RegistrationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.first_name = self.config.get("ACCOUNT", "first_name")
        self.last_name = self.config.get("ACCOUNT", "last_name")
        self.email = self.config.get("ACCOUNT", "email")
        self.password = self.config.get("ACCOUNT", "password")
        self.confirm_password = self.config.get("ACCOUNT", "confirmation_password")

    def fill_registration_form(self):
        self.driver.find_element(*RegistrationLocators.FIRST_NAME).clear()
        self.driver.find_element(*RegistrationLocators.FIRST_NAME).send_keys(self.first_name)
        self.driver.find_element(*RegistrationLocators.LAST_NAME).clear()
        self.driver.find_element(*RegistrationLocators.LAST_NAME).send_keys(self.last_name)
        self.driver.find_element(*RegistrationLocators.EMAIL).clear()
        self.driver.find_element(*RegistrationLocators.EMAIL).send_keys(self.email)
        self.driver.find_element(*RegistrationLocators.PASSWORD).clear()
        self.driver.find_element(*RegistrationLocators.PASSWORD).send_keys(self.password)
        self.driver.find_element(*RegistrationLocators.CONFIRMATION_PASSWORD).clear()
        self.driver.find_element(*RegistrationLocators.CONFIRMATION_PASSWORD).send_keys(self.confirm_password)
        self.driver.find_element(*RegistrationLocators.AGREEMENT).click()

    def perform_registration(self):
        self.driver.find_element(*RegistrationLocators.CREATE_ACCOUNT).click()
