Feature: Login to Mobile App
  As a user of the mobile app,
  I want to be able to enter my username and password and log in
  So that I can access my account and use the app's features.

  @regression @smoke @sanity
  Scenario: Successful Login
    Given the user insert credentials to be able access to the homepage screen
    Then the app should display the homepage screen

  @regression
  Scenario: Incorrect Password
    Given the user insert an incorrect password
    Then the app should display an error message

  @regression
  Scenario: Invalid Username
    Given the user is insert an incorrect username
    Then the app should display an error message