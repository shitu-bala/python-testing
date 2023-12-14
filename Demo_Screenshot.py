import  time
from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Demo_SreenShot:
     def capturescreenshot(self):

         driver = webdriver.Chrome()
         driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
         #driver.find_element(By.XPATH,"//input[@id='login-input']")
         conti_demo= driver.find_element(By.XPATH,"//button[@id='login-continue-btn']")
         conti_demo.screenshot(".\\test.png")
         conti_demo.click()
         time.sleep(4)
         driver.get_screenshot_as_file(".\\test2.png")
         driver.save_screenshot(".\\test4.png")

A1= Demo_SreenShot()
A1.capturescreenshot()