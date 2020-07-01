from behave import Given, When, Step, Then


@Given("I'm on the Magento home page")
def step_impl(context):
    context.page.open_home_page()


@When('I enter "{xd}" email address')
def step_impl(context, xd):
    if xd == "correct":
        context.page.set_newsletter_email("correctemail@correctemail.com")
    elif xd == "incorrect":
        context.page.set_newsletter_email("incorrectemail@")
    elif xd == " ":
        context.page.set_newsletter_email(" ")


@Step("I click Sign up button")
def step_impl(context):
    context.page.join_to_newsletter()


@Then("I should see message with confirmation")
def step_impl(context):
    assert False


@Then("I should see message 'Podaj poprawny adres email (Np: jan@kowalski.pl).'")
def step_impl(context):
    context.page.check_error_message_displayed("Podaj poprawny adres email (Np: jan@kowalski.pl).")


@Then("I should see message 'To jest wymagane pole.'")
def step_impl(context):
    context.page.check_error_message_displayed("To jest wymagane pole.")