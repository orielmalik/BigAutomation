Feature: Test GeeksForGeeks website

  Scenario: Searching in GeeksForGeeks
    Given I open GeeksForGeeks homepage
    When I search for "gaya"
    Then the unittest for Selenium should pass
