Feature: DETAILS_ABOUT_ANY_ITEM

    @regresion
    Scenario: DETAILS_ABOUT_ANY_ITEM
      Given we are in "Productos" scree
      When we tap on the first item
      Then we validate that the price and the product name are correct

