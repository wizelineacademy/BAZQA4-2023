Feature: Shopping_cart
  As a shopper
  I want to be able to choose a product
  So that I can add it to my cart and purchase it

  Background:
  Given the user insert credentials to be able access to the homepage screen

  @e2e @regression
  Scenario: Buy a product
        Given click on Add to Car Button from Dashboard
        When click on Icon Car
        And click on checkout button
        And fill the information forms
        And click on Continue Button
        And click on Finish Button
        Then validate the checkout successful