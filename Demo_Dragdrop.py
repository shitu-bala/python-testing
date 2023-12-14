import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class Slider_move:
    def sliderevent(self):
        driver = webdriver.Chrome()
        driver.get("https://jqueryui.com/droppable/")
        driver.maximize_window()
        driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@class='demo-frame']"))
        elem1= driver.find_element(By.XPATH,"//div[@id='draggable']")
        elem2 = driver.find_element(By.XPATH,"//div[@id='droppable']")
        #ActionChains(driver).drag_and_drop(elem1,elem2).perform()
        ActionChains(driver).drag_and_drop_by_offset(elem1,160,25).perform()
        time.sleep(5)
obj1= Slider_move()
obj1.sliderevent()