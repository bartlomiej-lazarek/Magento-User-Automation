from selenium import webdriver

from pages.authentication_page import AuthenticationPage
from pages.base_page import BasePage
from pages.registration_page import RegistrationPage


def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(5)

    if "home_page" in scenario.tags:
        context.home_page = BasePage(context.driver)
    if "authentication_page" in scenario.tags:
        context.auth_page = AuthenticationPage(context.driver)
    if "registration_page" in scenario.tags:
        context.registration_page = RegistrationPage(context.driver)


def after_scenario(context, scenario):
    context.driver.quit()


