Feature: Login

  @e2e
  Scenario: Login
    Given we are in login screen
    When we entering valid credentials
    Then we see Products screen
