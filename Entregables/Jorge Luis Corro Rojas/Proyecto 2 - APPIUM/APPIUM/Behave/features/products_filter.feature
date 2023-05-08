Feature: FILTER_PRODUCT_LIST

      @Regression
      Scenario: Filter_price_high_to_low
            Given we are in the "Productos" screen
            When we tap on "Filtro" button
            And we tap in "Price (high to low)" option
            Then we validate that the list of products is sorted by the filter from hightest to lowest