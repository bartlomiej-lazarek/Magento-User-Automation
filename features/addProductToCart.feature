Feature: Add product to cart

  @home_page
  Scenario: Add simply product to cart using hover
    Given I'm on the Magento home page
    When I hover on the product
    And I click Add to Cart button
    Then I should see the success message

  @home_page
  Scenario: Add simply product to cart from product page
    Given I'm on the Magento home page
    When I click on the product
    And I click Add to Cart button
    Then I should see the success message

  @home_page
  Scenario: Add configurable product to cart, choose attribute using hover
    Given I'm on shop page with configurable products
    When I hover on the product
    And I click on one of attribute options
    And I click Add to Cart button
    Then I should see the success message

  @home_page
  Scenario: Add configurable product to cart, choose attribute from product page
    Given I'm on configurable product page
    When I click on one of attribute options
    And I click Add to Cart button
    Then I should see the success message

  @home_page
  Scenario: Add configurable product to cart, don't choose attribute from product page
    Given I'm on configurable product page
    When I click Add to Cart button
    Then I should see a message saying that choosing attribute option is required