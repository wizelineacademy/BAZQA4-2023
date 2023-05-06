Feature: ADD_A_PRODUCT_TO_THE_CAR

  @regresion

  Scenario: ADD_THE_FIRST_PRODUCT_TO_THE_CAR
    Given we are in the "Productos" screen
    When we tap on "Añadir a carrito" from the first item
    And we tap on the cart icon
    Then we validate that the product name from cart page is correct
    Then we validate that the amount is correct

