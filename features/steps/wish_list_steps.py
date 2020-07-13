from behave import Step, Then


@Step("I click on Add to wish list button")
def step_impl(context):
    context.home_page.add_to_wish_list()


@Then("I should be redirect to wish list page")
def step_impl(context):
    assert "/wishlist/index/" in context.driver.current_url


@Then("I should see a message saying that the product has been successfully added to wish list")
def step_impl(context):
    assert len(context.driver.find_elements_by_css_selector("div.message-success")) > 0
