import time
from selenium import  webdriver
from selenium.webdriver.common.by import By


class Demo_Iframe:
    def find_iframe(self):
        driver = webdriver.Chrome()
        driver.get("file://C:/Users/Arun/PycharmProjects/pythonautomation-testing/index.html")
        driver.maximize_window()
        window1=driver.current_window_handle
        driver.switch_to.frame(driver.find_element(By.ID,"newFrame"))
        test=driver.find_element(By.XPATH,"//input[@id='notes']")
        test.click()
        test.send_keys("shitu")
        time.sleep(3 )

        driver.switch_to.window(window1)
        driver.find_element(By.XPATH,"//input[@id='female']").click()

        time.sleep(3)
        #time.sleep(4)

Df = Demo_Iframe()

Df.find_iframe()
