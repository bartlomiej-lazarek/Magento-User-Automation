from selenium import webdriver

from pages.authentication_page import AuthenticationPage
from pages.cart_page import CartPage
from pages.checkout_pages import OrderSummaryPage, ShippingPage, PaymentPage
from pages.home_page import HomePage
from pages.registration_page import RegistrationPage


def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(5)

    if "skip" in scenario.tags:
        scenario.skip("Marked with @skip")
        return
    if "home_page" in scenario.tags:
        context.home_page = HomePage(context.driver)
    if "authentication_page" in scenario.tags:
        context.authentication_page = AuthenticationPage(context.driver)
    if "registration_page" in scenario.tags:
        context.registration_page = RegistrationPage(context.driver)
    if "cart_page" in scenario.tags:
        context.cart_page = CartPage(context.driver)
    if "shipping_page" in scenario.tags:
        context.shipping_page = ShippingPage(context.driver)
    if "payment_page" in scenario.tags:
        context.payment_page = PaymentPage(context.driver)
    if "order_summary_page" in scenario.tags:
        context.order_summary_page = OrderSummaryPage(context.driver)


def after_scenario(context, scenario):
    context.driver.quit()


