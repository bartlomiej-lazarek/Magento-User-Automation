from behave import Given, When, Step, Then


@When('I enter "{email_type}" email address')
def step_impl(context, email_type):
    if email_type == "correct":
        context.page.set_newsletter_email("correctemail@correctemail.com")
    elif email_type == "incorrect":
        context.page.set_newsletter_email("incorrectemail@")
    elif email_type == " ":
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