Feature: CHECK_INFO_IN_THE_CAR

    @smoke
    Scenario: CHECK_INFO_IN_THE_CAR
      Given we are in the "PRODUCTOS" screen
      When we have items in the cart
      And we tap on the card icon
      Then we can see the info about the item