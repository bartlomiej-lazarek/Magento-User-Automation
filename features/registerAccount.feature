Feature: Register new account

  @home_page @authentication_page @registration_page
  Scenario: Successfully register new account
    Given I'm not logged in and I open login page
    When I click Create Account button
    And I enter all the required registration information
    And I click Create Account button in registration form
    Then I should be redirect to My Account page
    And I should see the success message

  @home_page @authentication_page @registration_page
  Scenario: Unsuccessfully register new account
    Given I'm not logged in and I open login page
    When I click Create Account button
    And I don't enter any the required registration information
    And I click Create Account button in registration form
    Then I should see a message saying that the registration information are required
