

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Find_ElementbyId:

    def locate_Element(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        time.sleep(10)
        elements_list = driver.find_elements(By.TAG_NAME, 'a')
        for i in elements_list:
            print(i.text)
        print(len(elements_list))

        time.sleep(5)


ob1 = Find_ElementbyId()


ob1.locate_Element()