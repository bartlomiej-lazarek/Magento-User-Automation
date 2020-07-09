from locators.locators import AuthenticationLocators
from pages.base_page import BasePage


class AuthenticationPage(BasePage):

    def login(self, email, password):
        self.driver.find_element(*AuthenticationLocators.EMAIL_INPUT).clear()
        self.driver.find_element(*AuthenticationLocators.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*AuthenticationLocators.PASSWORD_INPUT).clear()
        self.driver.find_element(*AuthenticationLocators.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*AuthenticationLocators.LOGIN_BUTTON).click()

    def open_create_account_form(self):
        self.driver.find_element(*AuthenticationLocators.CREATE_ACC_BUTTON).click()
