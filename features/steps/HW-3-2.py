from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='./chromedriver.exe')
from time import sleep
driver.get('https://www.amazon.com/')
driver.find_element(By.CLASS_NAME, 'a-input-text a-span12 auth-autofocus auth-required-field')

# email field
#driver.find_element(By.CSS_SELECTOR, "#ap_email")

#continue button
driver.find_element(By.CSS_SELECTOR, "continue")

#need help link
driver.find_element(By.CSS_SELECTOR, ".a-expander-prompt")

#Forgot your password link, this would need a comment to explain as the id does not
driver.find_element(By.CSS_SELECTOR, "auth-fpp-link-bottom")