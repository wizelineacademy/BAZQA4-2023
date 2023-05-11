Feature: Products
  As a shopper
  I want to be able to choose a product
  So that I can add it to my cart and purchase it

  Background:
  Given the user insert credentials to be able access to the homepage screen

  @regression @smoke
   Scenario: Validate product details after search
        Given Clik on a product
        Then Validate the product details

  @regression
    Scenario: Add a Product to the Cart
        Given Clik on a product
        When click on Add to Car Button
        And click on Icon Car
        Then Validate the attributes in the car

  @regression @sanity
    Scenario: Filter Products by Price Range
          Given click on Icon Filter
          When click on sort the price (low to high)
          Then Validate the filter is applied