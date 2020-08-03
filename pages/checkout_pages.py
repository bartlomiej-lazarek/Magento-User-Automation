import re
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as ec

from locators.locators import PaymentLocators, OrderSummaryLocators, CartLocators
from locators.locators import ShippingLocators
from pages.base_page import BasePage


class PaymentPage(BasePage):

    def choose_payment_type(self, payment_type):
        self.wait.until(ec.presence_of_element_located(PaymentLocators.LOADING_PAGE))
        if payment_type == "COD":
            self.driver.find_element(*PaymentLocators.COD).click()
        elif payment_type == "Bank Transfer Payment":
            self.driver.find_element(*PaymentLocators.BANK_TRANSFER).click()

    def proceed_to_checkout(self):
        self.driver.find_element(*PaymentLocators.PROCEED_TO_CHECKOUT).click()


class ShippingPage(BasePage):

    def fill_shipping_form(self):
        self.wait.until(ec.presence_of_element_located(PaymentLocators.LOADING_PAGE))
        self.driver.find_element(*ShippingLocators.CUSTOMER_EMAIL).clear()
        self.driver.find_element(*ShippingLocators.CUSTOMER_EMAIL).send_keys("testemail@emailtest.com")
        self.driver.find_element(*ShippingLocators.FIRST_NAME).clear()
        self.driver.find_element(*ShippingLocators.FIRST_NAME).send_keys("Jan")
        self.driver.find_element(*ShippingLocators.LAST_NAME).clear()
        self.driver.find_element(*ShippingLocators.LAST_NAME).send_keys("Kowalski")
        self.driver.find_element(*ShippingLocators.STREET).clear()
        self.driver.find_element(*ShippingLocators.STREET).send_keys("Street")
        self.driver.find_element(*ShippingLocators.STREET_NUMBER).clear()
        self.driver.find_element(*ShippingLocators.STREET_NUMBER).send_keys("5")
        self.driver.find_element(*ShippingLocators.CITY).clear()
        self.driver.find_element(*ShippingLocators.CITY).send_keys("TestCity")
        Select(self.driver.find_element(*ShippingLocators.COUNTRY)).select_by_value("PL")
        self.driver.find_element(*ShippingLocators.POST_CODE).clear()
        self.driver.find_element(*ShippingLocators.POST_CODE).send_keys("00-000")
        self.driver.find_element(*ShippingLocators.PHONE_NUMBER).clear()
        self.driver.find_element(*ShippingLocators.PHONE_NUMBER).send_keys("123123123")
        self.wait.until(ec.presence_of_element_located(CartLocators.LOADED_CHECKOUT))

    def confirm_shipping_data(self):
        self.wait.until(ec.presence_of_element_located(CartLocators.LOADED_CHECKOUT))
        self.driver.find_element(*ShippingLocators.PROCEED_TO_CHECKOUT).click()


class OrderSummaryPage(BasePage):

    def get_order_number(self):
        self.wait.until(ec.url_contains("/checkout/onepage/success/"))
        message = self.driver.find_element(*OrderSummaryLocators.ORDER_NUMBER).text
        return re.findall(r'\d+', message)
