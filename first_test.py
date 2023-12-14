from  selenium  import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

#driver.get("https://www.indianeagle.com/")
driver.get("https://www.redbus.in/")
print(driver.title)

src = driver.find_element(By.ID,"src")
src.send_keys("Delhi")
src.send_keys(Keys.ENTER)

dest = driver.find_element(By.ID, "dest")
dest.send_keys("Mumbai")
dest.send_keys(Keys.ENTER)
date_in = driver.find_element(By.ID,"onward_cal")
date_in.click()

cal_in = driver.find_element(By.ID,"rb-calendar_onward_cal")

day_in = driver.find_element(By.XPATH,"//td[@class='current day']")
print(day_in)
day_in.click()

search = driver.find_element(By.ID,"search_btn")
search.click()

#driver.close()