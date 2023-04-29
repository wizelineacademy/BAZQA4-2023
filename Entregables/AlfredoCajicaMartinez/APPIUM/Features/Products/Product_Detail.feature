Feature: Product detail

  Scenario: See product info screen
    Given we are in Products screen
    When we tap on any product
    Then we see Product info screen


  Scenario : See "Nombre" and "Precio" product info
    Given we are in Products screen
    When we tap on first product
    Then we see "Camisa Sauce Labs Bolt" name
    And "Get your testing superhero on with the Sauce Labs bolt T-shirt. From American Apparel, 100% ringspun combed cotton, heather gray with red bolt." description
    And "15.99" price


  #Reusuable scenario when we look for specific one
  Scenario Outline: See product info screen
    Given we are in Products screen
    When we tap on <Nombre> product
    Then we see Product info screen

    Examples: Valid Product
      | Nombre                 |
      | Camisa Sauce Labs Bolt |


  #Reusuable scenario when we look for specific one
  Scenario Outline: See "Nombre" and "Precio" product info
    Given we are in Products screen
    When we tap on <Nombre> product
    Then we see <Nombre>
    And <Precio>

    Examples: Valid product info
      | Nombre                           | Precio |
      | Camisa Sauce Labs Bolt           | 15.99  |
      | Camisa Test.allTheThings()(Roja) | 15.99  |
      | Chamarra Sauce Labs              | 49.99  |