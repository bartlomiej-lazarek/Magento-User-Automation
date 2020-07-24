from locators.locators import CustomerAccountLocators
from pages.authentication_page import AuthenticationPage


class CustomerAccountPage(AuthenticationPage):

    def open_change_password_form(self):
        self.driver.find_element(*CustomerAccountLocators.CHANGE_PASSWORD).click()

    def fill_change_password_form(self):
        self.driver.find_element(*CustomerAccountLocators.CURRENT_PASSWORD).send_keys(self.current_password)
        self.driver.find_element(*CustomerAccountLocators.NEW_PASSWORD).send_keys(self.new_password)
        self.driver.find_element(*CustomerAccountLocators.CONFIRM_PASSWORD).send_keys(self.new_password)

    def confirm_form(self):
        self.driver.find_element(*CustomerAccountLocators.SAVE_BUTTON).click()

    def login_and_save_new_password(self):
        self.fill_login_form("new_password")
        if "/customer/account/login" in self.driver.current_url:
            self.config.set("ACCOUNT", "current_password", self.new_password)
            with open('config.ini', 'w') as f:
                self.config.write(f)

    def logout(self):
        self.driver.find_element(*CustomerAccountLocators.LOGOUT).click()

    def go_to_newsletter_menu(self):
        self.driver.find_element(*CustomerAccountLocators.NEWSLETTER_MENU).click()

    def check_newsletter_checkbox(self):
        self.driver.find_element(*CustomerAccountLocators.SUBSCRIBE_CHECKBOX).click()

    def go_to_orders_menu(self):
        self.driver.find_element(*CustomerAccountLocators.ORDERS_MENU).click()

    def check_if_orders_displayed(self):
        return len(self.driver.find_elements(*CustomerAccountLocators.ORDERS)) > 0

    def go_to_address_menu(self):
        self.driver.find_element(*CustomerAccountLocators.ADDRESS_MENU).click()

    def open_delivery_address_form(self):
        self.driver.find_element(*CustomerAccountLocators.CHANGE_DELIVERY_ADDRESS).click()

    def set_new_street(self):
        self.driver.find_element(*CustomerAccountLocators.STREET_INPUT).clear()
        self.driver.find_element(*CustomerAccountLocators.STREET_INPUT).send_keys("newStreet")

    def get_delivery_address(self):
        return self.driver.find_element(*CustomerAccountLocators.DELIVERY_ADDRESS).text
