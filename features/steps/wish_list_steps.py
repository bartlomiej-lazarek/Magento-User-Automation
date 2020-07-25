from behave import Step, Then


@Step("I click on Add to wish list button")
def step_impl(context):
    context.home_page.add_to_wish_list()


@Then("I should be redirect to wish list page")
def step_impl(context):
    assert "/wishlist/index/" in context.driver.current_url
