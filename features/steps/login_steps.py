from behave import When, Step, Then


@When("I enter email and correct password")
def step_impl(context):
    context.authentication_page.fill_login_form(True)


@When("I enter email and incorrect password")
def step_impl(context):
    context.authentication_page.fill_login_form(False)


@Step("I click on Login button")
def step_impl(context):
    context.authentication_page.perform_login()


@Then("I should see a message saying that the given data are incorrect")
def step_impl(context):
    assert len(context.driver.find_elements_by_css_selector("div.message-error")) > 0
