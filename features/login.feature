Feature: Login in shop

  Scenario: Login using correct login and password
    Given I'm not logged in and I open login page
    When I enter email nad correct password
    And I click on Login button
    Then I should be redirect to My Account page

  Scenario: Login using incorrect password
    Given I'm not logged in and I open login page
    When I enter mail and incorrect password
    And I click on Login button
    Then I should see a message saying that the given data are incorrect

