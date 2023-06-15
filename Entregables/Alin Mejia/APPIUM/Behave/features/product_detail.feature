Feature: As a user I want to see the product details
    Background:
    Given we are logged in

  @smoke
  Scenario: PRODUCT_DETAILS
    Given we are in the "Home Pag" screen
    When we swipe down until we found the "Mochila Sauce Labs" product
    And we tap on the product card
    Then we validate the product title
    And the product price