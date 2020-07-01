from selenium import webdriver

from pages.base_page import BasePage


def after_scenario(context, feature):
    context.driver.quit()


def before_tag(context, tag):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(5)

    if tag.startswith("home"):
        context.page = BasePage(context.driver)
