Feature: Add product to shopping cart

  Scenario: Add product to shopping cart in Productos screen
    Given we are in Products screen
    When we tap on "AÑADIR A CARRITO" button in the first product
    Then we see "AÑADIR A CARRITO" text on the button changes to "REMOVER" text


  Scenario: Add product to shopping cart in Product info screen
    Given we are in Product info screen of the first product
    When we tap on "AÑADIR A CARRITO" button
    Then we see "AÑADIR A CARRITO" text on the button changes to "REMOVER" text


  Scenario Outline: Check the product listed in shopping cart
    Given we added the first product in shopping cart
    When we tap on shopping cart button
    Then we see <Producto> listed with <Precio>
    And <Cantidad>
    And <Descripcion>

    Examples: Valid product info
      | Producto               | Precio | Cantidad | Descripcion                                                                                                                                     |
      | Camisa Sauce Labs Bolt | 15.99  | 1        | Get your testing superhero on with the Sauce Labs bolt T-shirt. From American Apparel, 100% ringspun combed cotton, heather gray with red bolt. |
