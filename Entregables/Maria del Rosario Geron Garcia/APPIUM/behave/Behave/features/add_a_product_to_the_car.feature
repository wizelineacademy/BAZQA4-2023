Feature: ADD_A_PRODUCT_TO_THE_CAR

  @Regression
  #@smoke
  Scenario: ADD_THE_FIRST_PRODUCT_TO_THE_CAR
    Given we are in the "Productos" screen
    When we tap on "Añadir a carrito" from the first item
    And we tap on the card icon
    Then we validate that the product title is correct
    And we validate that the product price is correct into the cart