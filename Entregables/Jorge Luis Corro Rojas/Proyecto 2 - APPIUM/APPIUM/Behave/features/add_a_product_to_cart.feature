Feature: ADD_A_PRODUCT_TO_THE_CART

  @Regression
  Scenario: ADD_A_PRODUCT
    Given we are in the "Productos" screen
    When we tap on "Agregar a carrito" button from the first item
    And we tap on the cart icon
    Then we validate that the product title is correct

