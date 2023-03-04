from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='C:\Users\lubna khan\python-selenium-automation\chromedriver.exe')
from time import sleep

driver.get('https://www.amazon.com/')
sleep(4)
driver.find_element(By.CLASS_NAME, 'a-icon a-icon-logo')
driver.find_elements(By.XPATH, "//a[@href='/ref=nav_logo")
driver.find_element(By.XPATH, "//a")
driver.find_element(By.XPATH, "//*[@href='/ref=nav_logo")
driver.find_element(By.XPATH, "//*[@href='/ref=nav_logo' and @aria-label='Amazon']")
#driver.find_element(By.XPATH, "//a[contains(@href, 'nav_cs_bestsellers')]")

driver.find_element(By.CLASS_NAME, "a-expander-prompt")
driver.find_element(By.CLASS_NAME, "Need help?")
driver.find_element(By.XPATH, "//span[contains(text(), 'Need')]")
#Forgot your password
driver.find_element(By.ID, "auth-fpp-link-bottom")
#sign in link
driver.find_element(By.ID, "ap-other-signin-issues-link")
#create amazon account
driver.find_element(By.ID, "createAccountSubmit")
#conditions of use
driver.find_element(By.XPATH, "//a[contains(@href, 'condition_of_use')]")
#privacy notice
driver.find_element(By.XPATH, "//a[contains(@href, 'notification_privacy_notice')]")


