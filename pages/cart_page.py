from selenium.webdriver.support import expected_conditions as ec

from locators.locators import CartLocators
from pages.base_page import BasePage



class CartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.correct_coupon_code = self.config.get("ORDER", "discount_code")

    def check_total_price_in_summary(self):
        products_total_price = 0

        products_price = self.driver.find_elements(*CartLocators.PRODUCT_TOTAL_PRICE)
        for product in products_price:
            products_total_price += self.string_to_float_price(product.text)

        total_price_summary = self.string_to_float_price(
            self.driver.find_element(*CartLocators.TOTAL_PRODUCTS_PRICE).text)
        assert products_total_price == total_price_summary

    def increase_product_qty(self):
        self.driver.find_element(*CartLocators.CHANGE_QTY_PLUS).click()

    def decrease_product_qty(self):
        self.driver.find_element(*CartLocators.CHANGE_QTY_MINUS).click()

    def set_product_qty(self, product_qty):
        self.driver.find_element(*CartLocators.PRODUCT_QTY_INPUT).clear()
        self.driver.find_element(*CartLocators.PRODUCT_QTY_INPUT).send_keys(product_qty)

    def get_product_qty(self):
        return self.driver.find_element(*CartLocators.PRODUCT_QTY_INPUT).get_attribute("value")

    def get_product_price(self):
        return self.string_to_float_price(self.driver.find_element(*CartLocators.PRODUCT_PRICE).text)

    def get_product_total_price(self):
        return self.string_to_float_price(self.driver.find_element(*CartLocators.PRODUCT_TOTAL_PRICE).text)

    def recalculate_cart(self):
        self.driver.find_element(*CartLocators.UPDATE_CART).click()
        self.wait.until(ec.presence_of_element_located(CartLocators.LOADED_CHECKOUT))

    def calculate_product_total_price(self):
        product_qty = self.get_product_qty()
        product_price = self.get_product_price()

        return float(product_qty) * product_price

    def remove_product(self):
        self.driver.find_element(*CartLocators.DELETE_PRODUCT).click()
        self.wait.until(ec.presence_of_element_located(CartLocators.LOADED_CHECKOUT))

    def remove_all_products(self):
        self.driver.find_element(*CartLocators.CLEAR_CART).click()
        self.driver.switch_to.alert.accept()
        self.wait.until(ec.presence_of_element_located(CartLocators.LOADED_CHECKOUT))

    def get_number_of_products_in_cart(self):
        return len(self.driver.find_elements(*CartLocators.PRODUCTS))

    def back_to_home_page(self):
        self.driver.find_element(*CartLocators.CONTINUE_SHOPPING).click()

    def proceed_to_checkout(self):
        self.driver.find_element(*CartLocators.PROCEED_TO_CHECKOUT).click()
        self.wait.until(ec.presence_of_element_located(CartLocators.LOADED_CHECKOUT))

    def set_correct_coupon_code(self, correct):
        coupon_input = self.driver.find_element(*CartLocators.COUPON_CODE)
        coupon_input.clear()
        if correct:
            coupon_input.send_keys(self.correct_coupon_code)
        else:
            coupon_input.send_keys("incorrect_coupon")

    def confirm_coupon_code(self):
        self.driver.find_element(*CartLocators.CONFIRM_COUPON_CODE).click()
