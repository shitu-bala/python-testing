import  time
from selenium import webdriver
from  selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Demo_calender:
    def date_selection(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        time.sleep(2)
        arrival_city = driver.find_element(By.ID, "BE_flight_origin_city")
        arrival_city.click()

        arrival_city.send_keys("Mumbai")
        arrival_city.send_keys(Keys.ENTER)
        time.sleep(2)
        dest_city = driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        dest_city.send_keys("Bangalore")

        dest_city.send_keys(Keys.ENTER)
        time.sleep(2)

a1=Demo_calender()

a1.date_selection()