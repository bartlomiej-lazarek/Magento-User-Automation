Feature: Joining the newsletter

  @home_page
  Scenario: Join to the newsletter using correct email address
    Given I'm on the Magento home page
    When I enter "correct" email address
    And I click Sign up button
    Then I should see message with confirmation

  @home_page
  Scenario: Join to the newsletter using incorrect email address
    Given I'm on the Magento home page
    When I enter "incorrect" email address
    And I click Sign up button
    Then I should see message 'Podaj poprawny adres email (Np: jan@kowalski.pl).'

  @home_page
  Scenario: Join to the newsletter without filling email address
    Given I'm on the Magento home page
    When I enter "empty" email address
    And I click Sign up button
    Then I should see message 'To jest wymagane pole.'

