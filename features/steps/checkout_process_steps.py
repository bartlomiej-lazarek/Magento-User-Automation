from behave import Step, Then


@Step("I set all shipping data")
def step_impl(context):
    context.shipping_page.fill_shipping_form()


@Step("I confirm shipping data and shipping carrier")
def step_impl(context):
    context.shipping_page.confirm_shipping_data()


@Step('I choose "{payment_type}" payment type')
def step_impl(context, payment_type):
    context.payment_page.choose_payment_type(payment_type)


@Step('I confirm order')
def step_impl(context):
    context.payment_page.proceed_to_checkout()


@Then('I should see a message with order number')
def step_impl(context):
    assert context.order_summary_page.get_order_number()
