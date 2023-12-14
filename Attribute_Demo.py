import time
from selenium import webdriver
class Find_Attribute:
    pass
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def value_attribute(self):
    driver = webdriver.Chrome()
    driver.get("https://www.yatra.com/")
    val_att=driver.find_element(By.XPATH,"//div[@id='credit-shellBtnID']//input[@id='BE_flight_flsearch_btn']").get_attribute("value")
    print(val_att)
v1 = Find_Attribute()
v1.value_attribute()



















