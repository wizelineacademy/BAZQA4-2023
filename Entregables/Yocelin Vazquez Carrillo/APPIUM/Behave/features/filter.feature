Feature: Filter

  @regresion
  Scenario: filtered_from_lowest_to_highest
    Given we are in the "Productos" screen
    When we tap on the icon filter
    And we select filter Price (low to high)
    Then we validate if the items are ordered

