Feature: ADD_A_PRODUCT_TO_THE_CAR

  Background:
    Given we are in the Home Page

  @smoke
  Scenario: ADD_THE_FIRST_PRODUCT_TO_THE_CAR
    Given we are in the "home" screen
    When we tap on "Añadir a carrito" from the first item
    And we tap on the card icon
    Then we validate that the product title is correct
