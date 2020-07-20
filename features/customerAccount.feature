Feature: Customer Account

  Scenario: Change password
    Given I'm logged user
    When I click on the change password
    And I set fields in change password section
    And I click save
    And I logout
    Then I should successfully login using new password

  Scenario: Join to the newsletter
    Given I'm logged user
    When I go to newsletter menu
    And I click on newsletter checkbox
    And I click save
    Then I should see a message saying that I successfully joined to the newsletter

  Scenario: Change delivery address
    Given I'm logged user
    When I go to address  menu
    And I click on change delivery address
    And I set new street
    And I click save address
    Then I should see a message saying that I successfully changed address
    And I should see new street in address menu

  Scenario: See recent orders
    Given I'm logged user
    When I go to my orders menu
    Then I should see list of my orders