import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Check_HiddenElement:
     def Enable_Displayed(self):
         driver = webdriver.Chrome()
         driver.get("https://www.yatra.com/hotels")
         result = driver.find_element(By.XPATH,"//i[@class='icon icon-angle-right arrowpassengerBox']").click()
         time.sleep(3)
         driver.find_element(By.XPATH, "//div[@class='hotel_passengerBox dflex relative']//div[3]//div[1]//div[1]//span[2]").click()
         time.sleep(3)
         Result1 = driver.find_element(By.XPATH,"//select[@class='ageselect']")
         print(Result1.is_displayed())

         driver.find_element(By.XPATH,"//div[@class='hotel_passengerBox dflex relative']//div[3]//div[1]//div[1]//span[1]").click()
         time.sleep(4)
         print(Result1.is_displayed())
         #print(Result1.is_displayed())



h1 = Check_HiddenElement()
h1.Enable_Displayed()


