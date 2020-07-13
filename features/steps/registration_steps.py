from behave import Given, Step, Then


@Given("I'm not logged in and I open login page")
def step_impl(context):
    context.home_page.open_home_page()
    context.home_page.go_to_authentication_page()


@Then("I click Create Account button")
def step_impl(context):
    context.auth_page.open_create_account_form()


@Step("I enter all the required registration information")
def step_impl(context):
    context.registration_page.fill_registration_form()


@Step("I click Create Account button in registration form")
def step_impl(context):
    context.registration_page.perform_registration()


@Step("I should see a message saying that the account has been successfully created")
def step_impl(context):
    assert len(context.driver.find_elements_by_css_selector(".message-success")) > 0


@Step("I don't enter any the required registration information")
def step_impl(context):
    pass


@Then("I should see a message saying that the registration informations are required")
def step_impl(context):
    assert len(context.driver.find_elements_by_css_selector("div.mage-error")) > 0
