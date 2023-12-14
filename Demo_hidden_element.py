import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Check_HiddenElement:
     def Enable_Displayed(self):
         driver = webdriver.Chrome()
         driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
         result = driver.find_element(By.XPATH,"//button[@class='ws-btn w3-hover-black w3-dark-grey']")
         Result1=driver.find_element(By.XPATH,"//div[@id='myDIV']")
         print(Result1.is_displayed())
         result.click()
         print(Result1.is_displayed())



h1 = Check_HiddenElement()
h1.Enable_Displayed()