Feature: As a user I want to see the product details
    Background:
    Given we are logged in

  @e2ew
  Scenario: PRODUCT_DETAILS
    Then we swipe down until we found the "Mochila Sauce Labs" product
    And we tap on the product card
    Then we validate the product title
    And the product price