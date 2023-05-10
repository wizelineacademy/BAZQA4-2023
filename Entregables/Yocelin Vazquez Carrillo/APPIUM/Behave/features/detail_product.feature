Feature: Product_Detail

  @regresion
  Scenario: validate_product_detail
    Given we are in the "Productos" screen
    When we tap on the second product
    Then we validate that the product detail is displayed
    And we validate that the product name from detail page is correct
