Feature: ORDER_PRODUCT


  @e2e
     Scenario: ORDER_PRODUCT_FROM_SMALLEST_TO_LARGEST
     Given we are in the list the "Productos" screen
     When we tap on the filter icon
     And we tap on "Price (low to high)"
     Then we validate that the price order is correct