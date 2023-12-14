import  time
from selenium import webdriver
from selenium.webdriver.common.by import By


class Checkbox_demo:

    def find_checkbox(self):
        driver = webdriver.Chrome()
        driver.get("https://www.sugarcrm.com/request-demo/")
        driver.maximize_window()
        time.sleep(9)
        Checkbox = driver.find_element(By.ID,"doi0")
        print(Checkbox.is_selected())
        Checkbox.click()
        time.sleep(5)
        print(Checkbox.is_selected())







Ob1= Checkbox_demo()
Ob1.find_checkbox()