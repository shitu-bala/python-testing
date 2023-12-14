import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Find_ElementbyId:

    def locate_Element(self):
        driver = webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element(By.CSS_SELECTOR,".yt-sme-mobile-input").send_keys("shitubla@gmail.com")
        driver.find_element(By.CSS_SELECTOR, ".main-btn").click()
        time.sleep(5)
ob1= Find_ElementbyId()
ob1.locate_Element()