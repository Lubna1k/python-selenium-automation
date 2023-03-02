from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='Absolute Path')
from time import sleep

driver.get('https://www.amazon.com/')
sleep(5)
driver.find_element(By.ID,'twotabsearchtextbox').send_keys('table')
driver.find_element(By.ID, 'nav-search-submit-button').click(),