import time
from  selenium import  webdriver
from selenium.webdriver.common.by import By
from  selenium.webdriver.common.keys import Keys

class Demo_Calende:
    def select_date(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        time.sleep(5)
        depart_city = driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_city']")
        depart_city.click()
        time.sleep(3)
        depart_city.send_keys("Mumbai")
        depart_city.send_keys(Keys.ENTER)
        time.sleep(5)
        arrival_city = driver.find_element(By.XPATH,"//input[@id='BE_flight_arrival_city']")
        arrival_city.click()
        arrival_city.send_keys("Bangalore ")
        arrival_city.send_keys(Keys.ENTER)
        time.sleep(5)

        driver.find_element(By.XPATH, "//label[@for='BE_flight_origin_date']").click()
        time.sleep(4)

        driver.find_element(By.XPATH, "//td[@id='06/03/2023']").click()
        time.sleep(5)


C1 =Demo_Calende()
C1.select_date()