Feature: Login in shop

  @home_page @authentication_page
  Scenario: Login using correct login and password
    Given I'm not logged in and I open login page
    When I enter email and correct password
    And I click on Login button
    Then I should be redirect to My Account page

  @home_page @authentication_page
  Scenario: Login using incorrect password
    Given I'm not logged in and I open login page
    When I enter email and incorrect password
    And I click on Login button
    Then I should see a message saying that the given data are incorrect

