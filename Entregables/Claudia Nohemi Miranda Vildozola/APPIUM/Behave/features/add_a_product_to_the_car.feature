Feature: ADD_A_PRODUCT_TO_THE_CAR

  @e2e
    Scenario: ADD_THE_FIRST_PRODUCT_TO_THE_CARD
      Given we are in the "Productos" screen
      When we tap on "Anadir a carrito" from the first item
      And we tap on the card icon
      Then we validate that the product name is correct
      And we validate that the product price is correct