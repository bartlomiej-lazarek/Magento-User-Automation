import time
from selenium.webdriver.support import expected_conditions as ec

from locators.locators import ProductsListLocators, CartLocators
from pages.base_page import BasePage


class ProductsListPage(BasePage):

    def set_sort_products(self, sort_by):
        self.driver.find_element(*ProductsListLocators.SHOW_SORT_OPTIONS).click()
        time.sleep(1)
        self.driver.find_element_by_css_selector(f"[data-value={sort_by}]").click()

    def check_price_sorting(self, sort_by):
        self.wait.until(ec.presence_of_element_located(CartLocators.LOADED_CHECKOUT))
        prices_list = [self.string_to_float_price(price.text)
                       for price in self.driver.find_elements(*ProductsListLocators.PRODUCT_PRICE)]

        if sort_by == "low_to_high":
            return prices_list == sorted(prices_list)
        elif sort_by == "high_to_low":
            return prices_list == sorted(prices_list, reverse=True)

    def show_filter_options(self):
        self.driver.find_element(*ProductsListLocators.SHOW_FILTERS).click()

    def next_page(self):
        self.wait.until(ec.presence_of_element_located(CartLocators.LOADED_CHECKOUT))
        if len(self.driver.find_elements(*ProductsListLocators.NEXT_PAGE)) > 0:
            self.driver.find_element(*ProductsListLocators.NEXT_PAGE).click()
            return True

    def set_filter_size(self, size):
        self.driver.find_element_by_css_selector(f"[attribute-code='rozmiar'] a[aria-label='{size}']").click()

    def check_filtered_products(self, size):

        products_on_page = len(self.driver.find_elements(*ProductsListLocators.PRODUCT_PRICE))
        selected_size = len(self.driver.find_elements_by_css_selector(f"div.selected[aria-label='{size}']"))
        assert products_on_page == selected_size

        if self.next_page():
            self.check_filtered_products(size)
