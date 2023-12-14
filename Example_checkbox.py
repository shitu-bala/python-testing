import time
from selenium import webdriver
from  selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By


class Checkbox_demo:

    def find_checkbox(self):
        driver = webdriver.Chrome()
        driver.get("file://C:/Users/Arun/PycharmProjects/pythonautomation-testing/index.html")
        driver.maximize_window()
        time.sleep(4)
        male_radio = driver.find_element(By.ID,"male")
        print(male_radio.is_selected())
        male_radio.click()
        time.sleep(5)
        print(male_radio.is_selected())
        cars_dd = driver.find_element(By.ID, "cars")
        cars_dd.click()
        time.sleep(4)







Ob1= Checkbox_demo()
Ob1.find_checkbox()