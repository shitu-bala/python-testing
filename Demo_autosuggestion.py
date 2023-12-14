import  time
from selenium import webdriver
from  selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Auto_Sugg:
    def autosuggedtion(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        text=driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_city']")
        text.click()
        time.sleep(4)
        text.send_keys("New delhi")
        text.send_keys(Keys.ENTER)
        time.sleep(4)
        Going_To= driver.find_element(By.XPATH,"//input[@id='BE_flight_arrival_city']")

        time.sleep(4)
        Going_To.send_keys("new")
        Search_result = driver.find_elements(By.XPATH,"//div[@class='viewport']//div[1]/LI")
        #print(len(Search_result))

        time.sleep(4)
        for results in Search_result:
            print(results.text)
            if "New York (JFK)" in results.text:
                results.click()
                time.sleep(7)
                break
        driver.find_element(By.XPATH, "//label[@for='BE_flight_origin_date']").click()
        time.sleep(4)

        driver.find_element(By.XPATH, "//td[@id='06/03/2023']").click()
        time.sleep(5)

A1 = Auto_Sugg ()
A1.autosuggedtion()
