Feature: CLICK_ON_AN_ARTICLE

  @e2e
    Scenario: ARTICLE_INFORMATION
      Given we are in the "Article" screen
      When we tap in the firt article from the first item
      Then we validate that the article name is correct