

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class Double_click:
    def mouse_rightclick(self):
        driver = webdriver.Chrome()
        driver.get("https://demo.guru99.com/")
        driver.maximize_window()
        Rightclick= driver.find_element(By.XPATH,"//tbody/tr/td[1]/a[1]/img[1]")
        achains=ActionChains(driver)
        achains.context_click(Rightclick).perform()
        time.sleep(4)
        #double click
        achains = ActionChains(driver)
        achains.double_click()
        time.sleep(4)


D1= Double_click()
D1.mouse_rightclick()