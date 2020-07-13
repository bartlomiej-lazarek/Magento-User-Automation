from locators.locators import AuthenticationLocators
from pages.base_page import BasePage


class AuthenticationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.login_email = self.config.get("ACCOUNT", "login_email")
        self.correct_login_password = self.config.get("ACCOUNT", "correct_login_password")

    def fill_login_form(self, correct_password):
        self.driver.find_element(*AuthenticationLocators.EMAIL_INPUT).clear()
        self.driver.find_element(*AuthenticationLocators.EMAIL_INPUT).send_keys(self.login_email)
        self.driver.find_element(*AuthenticationLocators.PASSWORD_INPUT).clear()
        if correct_password:
            self.driver.find_element(*AuthenticationLocators.PASSWORD_INPUT).send_keys(self.correct_login_password)
        else:
            self.driver.find_element(*AuthenticationLocators.PASSWORD_INPUT).send_keys("incorrectPassword")

    def perform_login(self):
        self.driver.find_element(*AuthenticationLocators.LOGIN_BUTTON).click()

    def open_create_account_form(self):
        self.driver.find_element(*AuthenticationLocators.CREATE_ACC_BUTTON).click()
