from behave import Step


@Step("I click on Add to wish list button")
def step_impl(context):
    context.home_page.add_to_wish_list()
