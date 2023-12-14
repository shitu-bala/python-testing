import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Check_button:
     def Enable_button(self):
         driver = webdriver.Chrome()
         driver.get("https://training.openspan.com/login")
         result = driver.find_element(By.XPATH,"//input[@id='login_button']")
         print(result.is_enabled())
         driver.find_element(By.XPATH,"//input[@id='user_name']").send_keys("test@example.com")
         time.sleep(3)
         driver.find_element(By.XPATH, "//input[@id='user_pass']").send_keys("test@exam12")
         time.sleep(3 )
         print(result.is_enabled())




E1 = Check_button()
E1.Enable_button()