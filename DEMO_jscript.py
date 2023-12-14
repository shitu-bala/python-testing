import time
from selenium import webdriver

class Demo_js:
     def excute_script(self):
         driver = webdriver.Chrome()
         driver.execute_script("window.open('https://www.rcvacademy.com/elearning/','_self');")
         time.sleep(2)
         Demo_variable = driver.execute_script(" return document.getElementsByTagName('p')[1];")
         driver.execute_script("arguments[0].click();",Demo_variable )
         time.sleep(8)
jsE1= Demo_js()
jsE1.excute_script()