from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='./chromedriver.exe')
driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')

from  time import sleep
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


