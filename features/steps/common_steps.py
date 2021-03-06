from behave import Given, When, Then, Step


@Given("I'm on the Magento home page")
def step_impl(context):
    context.home_page.open_home_page()


@Given("I'm not logged in and I open login page")
def step_impl(context):
    context.home_page.open_home_page()
    context.home_page.go_to_authentication_page()


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


@Then("I should be redirect to My Account page")
def step_impl(context):
    assert "/customer/account/index/" in context.driver.current_url


@Given("I'm logged user")
def step_impl(context):
    context.home_page.open_home_page()
    context.home_page.go_to_authentication_page()
    context.authentication_page.fill_login_form("current_password")
    context.authentication_page.perform_login()


@Step('I add "{qty}" products to cart')
def step_impl(context, qty):
    context.home_page.add_to_cart_x_products(int(qty))


@Then("I should be redirected to home page")
def step_impl(context):
    assert context.home_page.home_url in context.driver.current_url


@Then("I should be redirected to checkout-shipping page")
def step_impl(context):
    assert "/checkout/#shipping" in context.driver.current_url


@Then("I should see the success message")
def step_impl(context):
    assert context.home_page.check_if_success_msg_displayed()


@Then("I should see the error message")
def step_impl(context):
    assert context.home_page.check_if_error_msg_displayed()
