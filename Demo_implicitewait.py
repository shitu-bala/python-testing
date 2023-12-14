import time
from selenium import webdriver
from selenium.webdriver.common.by import By
class DemoWaitImplicite:
    def implicitwait(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        driver.get("https://login.salesforce.com/?locale=ca")
        driver.find_element(By.XPATH,"//input[@id='username']").send_keys("shitu bala")


obj1= DemoWaitImplicite()
obj1.implicitwait()