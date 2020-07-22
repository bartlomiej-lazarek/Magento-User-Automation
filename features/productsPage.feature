Feature: Operation on products page

  @home_page @products_list_page
  Scenario: Sort products by price
    Given I'm on the products list page
    When I choose price min to max from sort list
    Then Products should be sorted by price from low to high

  @home_page @products_list_page
  Scenario: Filter products by size
    Given I'm on the products list page
    When I click on Filter
    And I choose M size
    Then Only products with that size should be displayed

  Scenario: Change number of products displayed on page
    Given I'm on the products list page
    When I change products list limit to 15 from 9
    Then Up to 15 products should be displayed
    And In the url address should be 'product_list_limit-15'
