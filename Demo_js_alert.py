import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class Demo_alert:
    def handlealert(self):
        driver = webdriver.Chrome()
        driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_confirm")
        driver.maximize_window()
        driver.switch_to.frame("iframeResult")
        driver.find_element(By.XPATH,"//button[normalize-space()='Try it']").click()
        time.sleep(5)
        driver.switch_to.alert.dismiss()
        time.sleep(5)
alert1 = Demo_alert()
alert1.handlealert()



