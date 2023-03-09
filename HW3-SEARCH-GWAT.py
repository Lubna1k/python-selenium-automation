from selenium.webdriver.common.by import By
from behave import given, when, then
from  selenium.webdriver.chrome.service import service

from time import sleep

@given('open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when('input text Doll')
def input_search_word(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('Doll')

@then('verify that text "Doll" is shown')
def verify_search_result(context):
     'expected_result = '"Doll"








