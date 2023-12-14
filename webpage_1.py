from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
#driver.get("https://www.indianeagle.com/")
driver.get("https://google.com")
print(driver.title)
#search_bar = driver.find_element(By.NAME,"q")
search_bar = driver.find_element(By.XPATH,"//input[@title='Search']")
search_bar.send_keys("Ayaan name meaning")
search_bar.send_keys(Keys.ENTER)
