Feature: ADD_A_PRODUCT_TO_THE_CART

    @regresion
    Scenario: ADD_A_PRODUCT_TO_THE_CART
      Given we are in the "Productos" screen
      When we tap on "Añadir a carrito" from the first item
      And we tap on the card icon
      Then we validate that the product title is correct