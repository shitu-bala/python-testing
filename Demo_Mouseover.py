import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class Mouse_over:
    def mouse_events(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        morebutton= driver.find_element(By.XPATH,"//span[@class='more-arr']")
        achains=ActionChains(driver)
        achains.move_to_element(morebutton).perform()
        time.sleep(4)
        driver.find_element(By.XPATH,"//span[normalize-space()='Adventures']").click()
        time.sleep(4)

mo = Mouse_over()
mo.mouse_events()