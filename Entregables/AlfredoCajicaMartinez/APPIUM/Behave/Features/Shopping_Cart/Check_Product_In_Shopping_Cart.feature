Feature: Check product in shopping cart

  @e2e
  Scenario: Check the first product listed in shopping cart
    Given we added the first product in shopping cart
    When we tap on shopping cart button
    Then we see "Get your testing superhero on with the Sauce Labs bolt T-shirt. From American Apparel, 100% ringspun combed cotton, heather gray with red bolt." product description
    And we see "1" qty
    And we see "$15.99" product price


  Scenario Outline: Check the first product listed in shopping cart
    Given we added the first product in shopping cart
    When we tap on shopping cart button
    Then we see "<Producto>" listed with "<Descripcion>"
    And we see "<Cantidad>"
    And we see "<Precio>"

    Examples: Valid product info
      | Producto               | Precio | Cantidad | Descripcion                                                                                                                                     |
      | Camisa Sauce Labs Bolt | 15.99  | 1        | Get your testing superhero on with the Sauce Labs bolt T-shirt. From American Apparel, 100% ringspun combed cotton, heather gray with red bolt. |