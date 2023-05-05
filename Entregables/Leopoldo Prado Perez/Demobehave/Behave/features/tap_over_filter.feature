Feature: PRODUCTS_BY_PRICE

      @n2n
      @regresion
      Scenario: PRODDUCTS_BY_PRICE
        Given we tap on the sort items button
        When we select the Price (low to high) option
        And we validate the lower price
        Then we validate the higher price