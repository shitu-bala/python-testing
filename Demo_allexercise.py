import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Demo_Test:
    def revisetest(self):
        driver = webdriver.Chrome()
        driver.get("https://www.indianeagle.com/")
        driver.maximize_window()
        time.sleep(4)
        driver.find_element(By.XPATH,"//span[@aria-label='One Way']").click()
        test= driver.find_element(By.XPATH,"//input[@id='sourceDiv']")
        test.send_keys("new ")
        driver.find_element(By.XPATH, "//p[contains(text(),'New York, NY - John F. Kennedy International Airpo')]")


        #test.click()
        #time.sleep(2)

        time.sleep(2)








OB1= Demo_Test()
OB1.revisetest()
