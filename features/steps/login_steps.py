from behave import When, Step


@When("I enter email and correct password")
def step_impl(context):
    context.authentication_page.fill_login_form("current_password")


@When("I enter email and incorrect password")
def step_impl(context):
    context.authentication_page.fill_login_form("incorrect_password")


@Step("I click on Login button")
def step_impl(context):
    context.authentication_page.perform_login()
