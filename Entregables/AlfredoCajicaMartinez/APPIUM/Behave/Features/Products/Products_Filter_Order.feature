Feature: Filter order

  @e2e
  Scenario: Sort by price low to high
    Given we are in Products screen
    When we tap on filter button
    And we tap on Price (low to high) button
    Then we see products sorted by price low to high
