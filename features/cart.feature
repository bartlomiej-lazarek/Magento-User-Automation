Feature: Operations in cart

  Background: Add 3 product to cart
    Given I'm on the Magento home page
    And I add "3" products to cart
    And I go to cart

  @home_page @cart_page
  Scenario: Check total price in summary
    Then The Sum of all products unit price should be equal to total price in summary section

  @home_page @cart_page
  Scenario: Change product quantity using + icon
    When I click on + icon
    Then Product quantity should be bigger by one

  @home_page @cart_page
  Scenario: Change product quantity using - icon
    When I click on - icon
    Then Product quantity should be less by one

  @home_page @cart_page
  Scenario: Recalculate cart
    When I set product qty to "5" using input field
    And  I click on Recalculate cart
    Then Product total sum should be equal to unit price times quantity

  @home_page @cart_page
  Scenario: Delete one product from cart
    When I click on trash icon in product row
    Then Should be 2 products in cart

  @home_page @cart_page
  Scenario: Delete all products from cart
    When I click on empty cart button
    Then Cart should be empty

  @home_page @cart_page
  Scenario: Add correct coupon code
    When I enter correct coupon code
    And I click confirm code button
    Then I should see the success message

  @home_page @cart_page
  Scenario: Add incorrect coupon code
    When I enter incorrect coupon code
    And I click confirm code button
    Then I should see the error message

  @home_page @cart_page
  Scenario: Back to the shop
    When I click back to shop button
    Then I should be redirected to home page

  @home_page @cart_page
  Scenario: Go to payment step
    When I click on proceed to checkout button
    Then I should be redirected to checkout-shipping page


