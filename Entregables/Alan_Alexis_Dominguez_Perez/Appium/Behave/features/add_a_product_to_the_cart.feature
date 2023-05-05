Feature: ADD_A_PRODUCT_TO_THE_CART
  Background:
    Given we are logged in

  @e2ew
  Scenario: ADD_THE_FIRST_PRODUCT_TO_THE_CART
    When we tap on "Añadir a carrito" from the first item
    And we tap on the cart icon
    Then we validate that the product title is correct
    And validate the description
    And validate price
