from behave import Given, When, Then, Step


@Given("I'm on the products list page")
def step_impl(context):
    context.home_page.go_to_products_list()


@When("I choose price min to max from sort list")
def step_impl(context):
    context.products_list_page.set_sort_products("low_to_high")


@Then("Products should be sorted by price from low to high")
def step_impl(context):
    assert context.products_list_page.check_price_sorting("low_to_high")


@When("I click on Filter")
def step_impl(context):
    context.products_list_page.show_filter_options()


@Step("I choose M size")
def step_impl(context):
    context.products_list_page.set_filter_size("M")


@Then("Only products with that size should be displayed")
def step_impl(context):
    context.products_list_page.check_filtered_products("M")
