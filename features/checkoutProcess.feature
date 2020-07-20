Feature: Checkout Process

  @home_page @cart_page @shipping_page @payment_page @order_summary_page
  Scenario: Purchase product by unregistered user with COD
    Given I'm on the Magento home page
    When I click on the product
    And I click Add to Cart button
    And I go to cart
    And I click on proceed to checkout button
    And I set all shipping data
    And I confirm shipping data and shipping carrier
    And I choose "COD" payment type
    And I confirm order
    Then I should see a message with order number

  @home_page @authentication_page @cart_page @shipping_page @payment_page @order_summary_page
  Scenario: Purchase product by logged user with bank transfer payment
    Given I'm logged user
    And I'm on the Magento home page
    When I click on the product
    And I click Add to Cart button
    And I go to cart
    And I click on proceed to checkout button
    And I confirm shipping data and shipping carrier
    And I choose "Bank Transfer Payment" payment type
    And I confirm order
    Then I should see a message with order number