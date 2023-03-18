from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='C:\Users\lubna khan\python-selenium-automation\chromedriver.exe')
from time import sleep

driver.get('https://www.amazon.com/')
sleep(4)
driver.find_element(By.ID,'twotabsearchtextbox').send_keys('tables')
driver.find_element(By.ID, 'nav-search-submit-button').click()