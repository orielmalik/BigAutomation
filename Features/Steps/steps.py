from behave import given, when, then
import unittest
from TESTS.SeleniumTestsOne import GeeksTest  # ייבוא המבחן שלך

@given('I open GeeksForGeeks homepage')
def step_open_homepage(context):
    context.target = GeeksTest()
    context.target.setUp()  # הפעלת ה-setup של Selenium

@when('I search for "{query}"')
def step_search_query(context, query):
    context.target.test_something()  # קריאה ישירה לבדיקה

@then('the unittest for Selenium should pass')
def step_unittest_pass(context):
    test_suite = unittest.TestLoader().loadTestsFromTestCase(GeeksTest)
    test_result = unittest.TextTestRunner().run(test_suite)
    assert test_result.wasSuccessful(), "Unittest failed!"
