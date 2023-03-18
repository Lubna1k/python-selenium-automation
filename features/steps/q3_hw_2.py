from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='./chromedriver.exe')
from time import sleep
driver.get('https://www.amazon.com/')


driver.find_element(By.ID, 'nav-orders').click()

sleep(4)

expected_result = 'Sign in'
actual_result = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
assert expected_result == actual_result, f'Expected {expected_result} but got {actual_result}'
driver.find_element(By.ID , 'ap_email')
