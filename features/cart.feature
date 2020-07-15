Feature: Operations in cart

  Background: Add 3 product to cart
    Given I'm on the Magento home page
    And I add '3' products to cart
    And I go to cart

  Scenario: Check total price in summary
    Then The Sum of all products unit price should be equal to total price in summary section

  Scenario: Change product quantity using + icon
    When I click on + icon
    Then Product quantity should be bigger by one

  Scenario: Change product quantity using - icon
    When I click on - icon
    Then Product quantity should be less by one

  Scenario: Recalculate cart
    When I set product qty to '5' using input field
    And  I click on Recalculate cart
    Then Product total sum should be equal to unit price times quantity

  Scenario: Delete one product from cart
    When I click on trash icon in product row
    Then This row should be deleted

  Scenario: Delete all products from cart
    When I click on empty cart button
    Then All products should be deleted

  Scenario: Add correct discount code
    When I enter correct discount code
    And I click confirm code button
    Then I should see a message saying that the discount code is correct

  Scenario: Add incorrect discount code
    When I enter incorrect  discount code
    And I click confirm code button
    Then I should see a message saying that the discount code is incorrect

  Scenario: Back to the shop
    When I click back to shop button
    Then I should be redirected to home page

  Scenario: Go to payment step
    When I click on proceed to checkout button
    Then I should be redirected to checkout-shipping page


