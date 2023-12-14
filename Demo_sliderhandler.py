import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class Slider_move:
    def sliderevent(self):
        driver = webdriver.Chrome()
        driver.get("https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_2_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_2_0_na_na_na&as-pos=2&as-type=TRENDING&suggestionId=mobiles&requestId=3eee9811-04e2-4066-975a-3f560836606b")
        driver.maximize_window()
        elem1= driver.find_element(By.XPATH,"//div[@class='_31Kbhn _28DFQy']//div[@class='_3FdLqY']")
        elem2= driver.find_element(By.XPATH,"//div[@class='_31Kbhn WC_zGJ']//div[@class='_3FdLqY']")
        time.sleep(4)
        ActionChains(driver).drag_and_drop_by_offset(elem2,-60,0).perform()
        #ActionChains(driver).click_and_hold(elem1).pause(1).move_by_offset(70,0).release().perform()
        time.sleep(5)






obj1= Slider_move()
obj1.sliderevent()