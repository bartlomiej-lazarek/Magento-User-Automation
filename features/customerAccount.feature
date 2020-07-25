Feature: Customer Account

  @home_page @authentication_page @customer_account_page
  Scenario: Change password
    Given I'm logged user
    When I click on the change password
    And I set fields in change password section
    And I click save
    And I logout
    And I open login page
    Then I should successfully login using new password

  @home_page @authentication_page @customer_account_page
  Scenario: Subscribe/Unsubscribe the newsletter from customer account page
    Given I'm logged user
    When I go to newsletter menu
    And I click on newsletter checkbox
    And I click save
    Then I should see the success message

  @home_page @authentication_page @customer_account_page
  Scenario: Change delivery address
    Given I'm logged user
    When I go to address menu
    And I click on change delivery address
    And I set new street
    And I click save
    Then I should see the success message
    And I should see new street in address menu

  @home_page @authentication_page @customer_account_page
  Scenario: See recent orders
    Given I'm logged user
    When I go to my orders menu
    Then I should see list of my orders