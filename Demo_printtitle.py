import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
class Title_name:
    def printtitlename(self):
        driver = webdriver.Chrome()
        driver.get("https://www.google.com/")
        print(driver.title)
        test= driver.find_element(By.NAME,"q")
        test.send_keys("air india")
        test.send_keys(Keys.ENTER)

w1= Title_name()
w1.printtitlename()
