Feature: Add product to shopping cart

  @e2e
  Scenario: Add product to shopping cart in Productos screen
    Given we are in Products screen
    When we tap on "AÑADIR A CARRITO" button in the first product
    Then we see "AÑADIR A CARRITO" text on the button changes to "REMOVER" text

  @e2e
  Scenario: Add product to shopping cart in Product info screen
    Given we are in Product info screen of the first product
    When we tap on "AÑADIR A CARRITO" button
    Then we see "AÑADIR A CARRITO" text on the button changes to "REMOVER" text
