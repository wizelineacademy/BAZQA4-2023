Feature: filter products

  Background:
    Given we are in the "LOGIN" screen
    When we fill the "Usuario" label
    And we fill the "Contraseña" label
    And we tap the "LOGIN" button
    Then we are in the "Productos" screen

  @e2e
  Scenario: ORDER_PRODUCTS_FILTER
    Given we can see the "Productos"
    When we tap the "filter" button
    And we see the the list options
    And we tap in "Price (low to high)" button
    Then we validate the order of products to Price (low to high)
