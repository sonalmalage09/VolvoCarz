Feature: Checkout Product

  @scheckout
  Scenario: Checkout product to cart
    Given I got navigated to Search Page Results
    When  I click on Add to cart button
    And verify cart details
    And product is checked out
    Then Verify warning message