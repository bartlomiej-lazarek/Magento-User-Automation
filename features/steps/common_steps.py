from behave import Given


@Given("I'm on the Magento home page")
def step_impl(context):
    context.page.open_home_page()