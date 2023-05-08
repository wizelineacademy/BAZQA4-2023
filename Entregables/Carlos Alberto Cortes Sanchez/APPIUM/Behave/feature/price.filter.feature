Feature: Sort products by price from lowest to highest

  @regression
  Scenario: Price from lowest to highest
    Given we select filter icon
    When we select the option low to high
    And scroll on the screen
    Then we validate the product with the highest price