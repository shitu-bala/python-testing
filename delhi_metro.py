from selenium.webdriver.common.by import By
from  selenium.webdriver.common.keys import Keys
from selenium import  webdriver

driver = webdriver.Chrome()
driver.get("https://www.gotransit.com/en/")
driver.maximize_window()
print(driver.title)

src = driver.find_element(By.XPATH ,"//input[@id='input-id1']")
src.send_keys("Burlington Go")
#src.send_keys(Keys.ENTER)

dest = driver.find_element(By.XPATH ,"//input[@id='input-id2']")
dest.send_keys("Oakville Go")
dest.send_keys(Keys.ENTER)


