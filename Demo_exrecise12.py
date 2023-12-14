import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from  selenium.webdriver.common.keys import Keys


class Findwindow:
    def find_element(self):
        driver = webdriver.Chrome()
        driver.get("file:///C:/Users/Arun/PycharmProjects/pythonautomation-testing/index.html")
        parent_handle= driver.current_window_handle
        driver.find_element(By.ID,"notworkinglink").click()
        time.sleep(4)
        all_handles= driver.window_handles

        for handle in all_handles:
            if handle != parent_handle:
                driver.switch_to.window(handle)
                print(parent_handle.title())
                test= driver.find_element(By.NAME,"q")
                test.send_keys("air india")
                test.send_keys(Keys.ENTER)



                time.sleep(4)
        driver.switch_to.window(parent_handle)
        driver.find_element(By.ID,"male").click()
        time.sleep(4)




w1 = Findwindow()
w1.find_element()


