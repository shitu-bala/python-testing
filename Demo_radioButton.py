import  time
from selenium import  webdriver
from  selenium.webdriver.common.by import By
from  selenium.webdriver.common.keys import Keys


class Demo_Radio:
     def radio_button(self):
         driver= webdriver.Chrome()
         driver.get("https://www.indianeagle.com/")
         driver.maximize_window()
         time.sleep(8)

         driver.find_element(By.XPATH,"//label[normalize-space()='Round Trip']//span[@role='button']").click()
         print(driver.find_element(By.XPATH, "//label[normalize-space()='One Way']//span[@role='button']").is_selected())
         time.sleep(5)
         driver.find_element(By.XPATH, "//label[normalize-space()='One Way']//span[@role='button']").click()
         time.sleep(5)
         print(driver.find_element(By.XPATH,"").is_selected())


w1 = Demo_Radio()
w1.radio_button()