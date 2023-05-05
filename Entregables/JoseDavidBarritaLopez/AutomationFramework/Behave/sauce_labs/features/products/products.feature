Feature: Products
  As a shopper
  I want to be able to choose a product
  So that I can add it to my cart and purchase it

  Background:
  Given the user insert credentials to be able access to the homepage screen
 @e2e
  Scenario: Validate product details after search
        Given Clik on a product
        Then Validate the product details

@e2e
 Scenario: Add a Product to the Cart
        Given Clik on a product
        When click on Add to Car Button
        And click on Icon Car
        Then Validate the attributes in the car

@e2e
Scenario: Filter Products by Price Range
        Given click on Icon Filter
        When click on sort the price (low to high)
        Then Validate the filter is applied


  @e2e
  Scenario: Buy a product
        Given click on Add to Car Button from Dashboard
        When click on Icon Car
        And click on checkout button
        And fill the information forms
        And click on Continue Button
        And click on Finish Button
        Then validate the checkout successful
