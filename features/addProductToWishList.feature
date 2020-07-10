Feature: Add product to wish list

  @home_page
  Scenario: Add product to wish list using hover as not logged  user
    Given I'm on the Magento home page
    When I hover on the product
    And I click on Add to wish list button
    Then I should be redirect to login page

  Scenario: Add product to wish list from product not logged user
    Given I'm on the Magento home page
    When I click on the product
    And I click on Add to wish list button
    Then I should be redirect to login page

  Scenario: Add product to wish list using hover as logged user
    Given I'm logged user
    And I'm on the Magento home page
    When I hover on the product
    And I click on Add to wish list button
    Then I should be redirect to wish list page
    And I should see a message saying that the product has been successfully added to wish list

  Scenario: Add product to wish list using hover as logged user
    Given I'm logged user
    And I'm on the Magento home page
    When I click on the product
    And I click on Add to wish list button
    Then I should be redirect to wish list page
    And I should see a message saying that the product has been successfully added to wish list