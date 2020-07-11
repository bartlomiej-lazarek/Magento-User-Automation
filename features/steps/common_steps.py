from behave import Given, When, Then, Step


@Given("I'm on the Magento home page")
def step_impl(context):
    context.home_page.open_home_page()


@When("I hover on the product")
def step_impl(context):
    context.home_page.hover_on_first_product()


@When("I click on the product")
def step_impl(context):
    context.home_page.click_on_first_product()


@Then("I should be redirect to login page")
def step_impl(context):
    assert "/customer/account/login" in context.driver.current_url


@Step("I click Add to Cart button")
def step_impl(context):
    context.home_page.add_to_cart()
