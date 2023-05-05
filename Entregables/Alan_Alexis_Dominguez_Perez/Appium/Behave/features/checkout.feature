Feature: Buy a product
    Background:
    Given we are logged in

    @e2e
    Scenario: BUY_A_PRODUCT
      Given we add a product to the cart
      Then we tap the "Checkout" button
      And we fill the "Nombre" field
      And we fill the "Apellido" field
      And we fill the "Código postal" field
      Then we tap the button "Continuar"
      Then we validate the product title from the information "Resume" screen
      Then we validate the product price from the information "Resume" screen
      Then we swipe down until we found the "Terminar" button
      And we tap the button "Terminar"
      Then we validate the successful screen is shown


