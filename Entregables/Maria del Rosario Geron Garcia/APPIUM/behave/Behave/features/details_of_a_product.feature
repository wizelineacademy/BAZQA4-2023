Feature: VIEW_DETAILS_OF_A_PRODUCT

  @e2e
  Scenario: TAP_THE_FIRST_PRODUCT_DETAILS
    Given we are in the "Productos" screen products
    When we tap on a "Producto" from the firts item
    And we validate that the product title is correct