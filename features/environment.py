from pathlib import Path
from selenium import webdriver
from datetime import datetime

from pages.authentication_page import AuthenticationPage
from pages.cart_page import CartPage
from pages.checkout_pages import OrderSummaryPage, ShippingPage, PaymentPage
from pages.customer_account_page import CustomerAccountPage
from pages.home_page import HomePage
from pages.products_list_page import ProductsListPage
from pages.registration_page import RegistrationPage


def before_all(context):
    create_folders_for_reports(context)


def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(5)

    create_page_objects(context, scenario)


def after_step(context, step):
    take_screenshots(context, step)


def after_scenario(context, scenario):
    context.driver.quit()
    create_test_report(scenario, context.report_path)


def create_page_objects(context, scenario):
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
    if "products_list_page" in scenario.tags:
        context.products_list_page = ProductsListPage(context.driver)
    if "customer_account_page" in scenario.tags:
        context.customer_account_page = CustomerAccountPage(context.driver)


def create_folders_for_reports(context):
    context.test_run_date = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    header_info = f"TEST REPORT {context.test_run_date}\n" \
                  f"RESULT  |FEATURE     |SCENARIO\n\n"

    context.report_path = Path(__file__).parent / f"..//reports//Test_report {context.test_run_date}"
    Path(context.report_path).mkdir(parents=True, exist_ok=True)
    context.failed_screenshots_path = Path(__file__).parent / f"{context.report_path}//screenshots//failed_tests"
    Path(context.failed_screenshots_path).mkdir(parents=True, exist_ok=True)
    context.successful_screenshots_path = Path(__file__).parent / f"{context.report_path}//screenshots//passed_tests"
    Path(context.successful_screenshots_path).mkdir(parents=True, exist_ok=True)

    with open(f"{context.report_path}//Report.txt", "w") as file:
        file.write(header_info)


def create_test_report(scenario, report_path):
    status = scenario.compute_status().name.upper()
    feature = scenario.feature.name
    scenario_info = f"{status} | {feature} | | {scenario.name}\n"

    with open(f"{report_path}//Report.txt", "a") as file:
        file.write(scenario_info)


def take_screenshots(context, step):
    if step.status == 'failed':
        context.driver.save_screenshot(f"{context.failed_screenshots_path}//{step.name}.jpg")
    if step.status == 'passed' and step.step_type == "then":
        context.driver.save_screenshot(f"{context.successful_screenshots_path}//{step.name}.jpg")
