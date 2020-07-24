from locators.locators import AuthenticationLocators
from pages.base_page import BasePage


class AuthenticationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.login_email = self.config.get("ACCOUNT", "login_email")
        self.current_password = self.config.get("ACCOUNT", "current_password")
        self.new_password = self.config.get("ACCOUNT", "new_password")

    def fill_login_form(self, password):
        self.driver.find_element(*AuthenticationLocators.EMAIL_INPUT).clear()
        self.driver.find_element(*AuthenticationLocators.EMAIL_INPUT).send_keys(self.login_email)
        self.driver.find_element(*AuthenticationLocators.PASSWORD_INPUT).clear()
        if password == "current_password":
            self.driver.find_element(*AuthenticationLocators.PASSWORD_INPUT).send_keys(self.current_password)
        elif password == "incorrect_password":
            self.driver.find_element(*AuthenticationLocators.PASSWORD_INPUT).send_keys("incorrectPassword")

    def perform_login(self):
        self.driver.find_element(*AuthenticationLocators.LOGIN_BUTTON).click()

    def open_create_account_form(self):
        self.driver.find_element(*AuthenticationLocators.CREATE_ACC_BUTTON).click()
