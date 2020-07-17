import time

from behave import Step, Then, When


@Step("I go to cart")
def step_impl(context):
    context.home_page.go_to_cart()


@Then("The Sum of all products unit price should be equal to total price in summary section")
def step_impl(context):
    context.cart_page.check_total_price_in_summary()


@When("I click on + icon")
def step_impl(context):
    context.product_qty_before = context.cart_page.get_product_qty()
    context.cart_page.increase_product_qty()


@When("I click on - icon")
def step_impl(context):
    context.product_qty_before = context.cart_page.get_product_qty()
    context.cart_page.decrease_product_qty()


@When('I set product qty to "{qty}" using input field')
def step_impl(context, qty):
    context.cart_page.set_product_qty(qty)


@Then("Product quantity should be bigger by one")
def step_impl(context):
    assert int(context.cart_page.get_product_qty()) == int(context.product_qty_before) + 1


@Then("Product quantity should be less by one")
def step_impl(context):
    assert int(context.cart_page.get_product_qty()) == int(context.product_qty_before) - 1


@Step("I click on Recalculate cart")
def step_impl(context):
    context.cart_page.recalculate_cart()


@Then("Product total sum should be equal to unit price times quantity")
def step_impl(context):
    # todo Have to wait until page will be reloaded
    time.sleep(5)
    assert context.cart_page.calculate_product_total_price() == context.cart_page.get_product_total_price()


@When("I click on trash icon in product row")
def step_impl(context):
    context.cart_page.remove_product()


@Then("Should be 2 products in cart")
def step_impl(context):
    # todo Have to wait until page will be reloaded
    time.sleep(5)
    assert context.cart_page.get_number_of_products_in_cart() == 2


@When("I click on empty cart button")
def step_impl(context):
    context.cart_page.remove_all_products()


@Then("Cart should be empty")
def step_impl(context):
    # todo Have to wait until page will be reloaded
    time.sleep(5)
    assert context.cart_page.get_number_of_products_in_cart() == 0


@When("I click back to shop button")
def step_impl(context):
    context.cart_page.back_to_home_page()


@When("I click on proceed to checkout button")
def step_impl(context):
    context.cart_page.proceed_to_checkout()


@When("I enter correct coupon code")
def step_impl(context):
    context.cart_page.set_correct_coupon_code(True)


@When("I enter incorrect coupon code")
def step_impl(context):
    context.cart_page.set_correct_coupon_code(False)


@Step("I click confirm code button")
def step_impl(context):
    context.cart_page.confirm_coupon_code()


@Step("I should see a message saying that the discount code is incorrect")
def step_impl(context):
    assert len(context.driver.find_elements_by_css_selector("div.message-error")) > 0


@Then("I should see a message saying that the discount code is correct")
def step_impl(context):
    assert len(context.driver.find_elements_by_css_selector("div.message-success")) > 0
