from behave import When, Step, Then


@When("I click on the change password")
def step_impl(context):
    context.customer_account_page.open_change_password_form()


@Step("I set fields in change password section")
def step_impl(context):
    context.customer_account_page.fill_change_password_form()


@Step("I click save")
def step_impl(context):
    context.customer_account_page.confirm_form()


@Step("I logout")
def step_impl(context):
    context.customer_account_page.logout()


@Step("I open login page")
def step_impl(context):
    context.home_page.open_home_page()
    context.home_page.go_to_authentication_page()


@Then("I should successfully login using new password")
def step_impl(context):
    context.customer_account_page.login_and_save_new_password()


@When("I go to newsletter menu")
def step_impl(context):
    context.customer_account_page.go_to_newsletter_menu()


@Step("I click on newsletter checkbox")
def step_impl(context):
    context.customer_account_page.check_newsletter_checkbox()


@Then("I should see a message saying that I successfully joined to the newsletter")
def step_impl(context):
    assert len(context.driver.find_elements_by_css_selector(".message-success")) > 0


@When("I go to my orders menu")
def step_impl(context):
    context.customer_account_page.go_to_orders_menu()


@Then("I should see list of my orders")
def step_impl(context):
    context.customer_account_page.check_if_orders_displayed()


@When("I go to address menu")
def step_impl(context):
    context.customer_account_page.go_to_address_menu()


@Step("I set new street")
def step_impl(context):
    context.customer_account_page.set_new_street()


@Step("I click on change delivery address")
def step_impl(context):
    context.customer_account_page.open_delivery_address_form()


@Then("I should see a message saying that I successfully changed address")
def step_impl(context):
    assert len(context.driver.find_elements_by_css_selector(".message-success")) > 0


@Then("I should see new street in address menu")
def step_impl(context):
    assert "newStreet" in context.customer_account_page.get_delivery_address()

