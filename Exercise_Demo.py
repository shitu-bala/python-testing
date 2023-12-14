import time
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

class Gmail_Demo:

    def Login_page(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/hotels")
        time.sleep(8)
        text1 =  driver.find_element(By.XPATH,"//h2[@class='big-title inlineBlock']").text
        print(text1)
        time.sleep(5)



ob1 = Gmail_Demo()
ob1.Login_page()
