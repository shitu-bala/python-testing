import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Find_browser:

    def Browser_Method(self):
        driver = webdriver.Chrome()
        driver.get("https://www.rcvacademy.com/")
        print(driver.title)
        driver.find_element(By.LINK_TEXT, "Courses").click()
        time.sleep(3)
        driver.back()
        time.sleep(3)
        driver.forward()
        driver.maximize_window()
        time.sleep(3)
        driver.fullscreen_window()


       # time.sleep()
ob1= Find_browser()
ob1.Browser_Method()