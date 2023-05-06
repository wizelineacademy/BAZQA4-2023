Feature: Filter

  @regresion
    @smoke
  Scenario: filtered_from_highest_to_lowest
    Given we are in the "Products" screen
    When we tap on the filter
    And we select filter Price (low to high and the high to low)
    Then we validate if the items are ordered

