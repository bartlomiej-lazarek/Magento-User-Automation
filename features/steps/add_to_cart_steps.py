from behave import Then, Given, Step


@Given("I'm on shop page with configurable products")
def step_impl(context):
    context.home_page.go_to_page_with_configurable_product_on_list()


@Step("I click on one of attribute options")
def step_impl(context):
    context.home_page.choose_first_attribute()


@Given("I'm on configurable product page")
def step_impl(context):
    context.home_page.go_to_configurable_product_page()


@Then("I should see a message saying that choosing attribute option is required")
def step_impl(context):
    assert len(context.driver.find_elements_by_css_selector("div.mage-error")) > 0
