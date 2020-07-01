Feature: Joining the newsletter

  Scenario: Join to the newsletter using correct email address
    Given I'm on the Magento home page
    When I enter correct email address
    And I click Sign up button
    Then I should see message with confirmation

  Scenario: Join to the newsletter using incorrect email address
    Given I'm on the Magento home page
    When I enter incorrect email address
    And I click Sign up button
    Then I should see message 'Podaj poprawny adres email (Np: jan@kowalski.pl).'

  Scenario: Join to the newsletter without filling email address
    Given I'm on the Magento home page
    Then I click Sign up button
    Then I should see message 'To jest wymagane pole.'

