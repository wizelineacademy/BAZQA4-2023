Feature: Filter

  @regresion
  Scenario: filtered_from_highest_to_lowest
    Given we are in the "Productos" screen
    When we tap on the filter
    And we select filter "Price(low to high) and (the high to low)"
    Then we validate if the items are ordered

