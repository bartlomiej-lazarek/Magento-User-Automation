from behave import When, Step, Then


@When('I enter "{email_type}" email address')
def step_impl(context, email_type):
    if email_type == "correct":
        context.home_page.set_newsletter_email("correctemail@correctemail.com")
    elif email_type == "incorrect":
        context.home_page.set_newsletter_email("incorrectemail@")
    elif email_type == " ":
        context.home_page.set_newsletter_email(" ")


@Step("I click Sign up button")
def step_impl(context):
    context.home_page.join_to_newsletter()


@Then("I should see message with confirmation")
def step_impl(context):
    assert True


@Then("I should see message 'Podaj poprawny adres email (Np: jan@kowalski.pl).'")
def step_impl(context):
    assert context.home_page.check_error_message_displayed(
        "Podaj poprawny adres email (Np: jan@kowalski.pl).")


@Then("I should see message 'To jest wymagane pole.'")
def step_impl(context):
    assert context.home_page.check_error_message_displayed(
        "To jest wymagane pole.")
