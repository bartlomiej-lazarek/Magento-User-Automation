from behave import Then

from locators.locators import ProductLocators


@Then("I should see a message saying that the product has been successfully added")
def step_impl(context):
    assert len(context.driver.find_elements(*ProductLocators.ADDED_PRODUCT_SUCCESS_MESSAGE)) > 0
