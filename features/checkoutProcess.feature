Feature: Checkout Process

  Scenario: Purchase product by unregistered user with COD
    Given I'm on the Magento home page
    When I click on the product
    And I click Add to Cart button
    And I go to cart
    And I click proceed to checkout button
    And I set all shipping data
    And I confirm shipping data and shipping carrier
    And I choose "COD" payment type
    And I confirm order
    Then I should see a message with order number

  Scenario: Purchase product by logged user with bank transfer payment
    Given I'm logged user
    And I'm on the Magento home page
    When I click on the product
    And I click Add to Cart button
    And I go to cart
    And I click proceed to checkout button
    And I confirm shipping data and shipping carrier
    And I choose "Bank Transfer Payment" payment type
    And I confirm order
    Then I should see a message with order number