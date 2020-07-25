Feature: Add product to wish list

  @home_page
  Scenario: Add product to wish list using hover as not logged  user
    Given I'm on the Magento home page
    When I hover on the product
    And I click on Add to wish list button
    Then I should be redirect to login page

  @home_page @skip
  Scenario: Add product to wish list from product page as not logged user
    Given I'm on the Magento home page
    When I click on the product
    And I click on Add to wish list button
    Then I should be redirect to login page

  @home_page @authentication_page
  Scenario: Add product to wish list using hover as logged user
    Given I'm logged user
    And I'm on the Magento home page
    When I hover on the product
    And I click on Add to wish list button
    Then I should be redirect to wish list page
    And I should see the success message

  @home_page @authentication_page @skip
  Scenario: Add product to wish list from product page as logged user
    Given I'm logged user
    And I'm on the Magento home page
    When I click on the product
    And I click on Add to wish list button
    Then I should be redirect to wish list page
    And I should see the success message