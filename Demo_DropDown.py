import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Selec
t

class Drop_Down:

    def select_option(self):

        driver = webdriver.Chrome()
        driver.get("file://C:/Users/Arun/PycharmProjects/pythonautomation-testing/index.html")

        driver.maximize_window()
        time.sleep(2)
        DD_demo = driver.find_element(By.ID,"cars")
        #time.sleep(5)

        #Select(DD_demo).select_by_value("audi")
        Select(DD_demo).select_by_value("audi")
        #time.sleep(3)
        #print(dd.select_by_value("audi"))
        time.sleep(2)



S1 = Drop_Down()

S1.select_option()

