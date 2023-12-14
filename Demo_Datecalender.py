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
        time.sleep(2)
        text.send_keys("New delhi")
        text.send_keys(Keys.ENTER)
        time.sleep(2)
        Going_To= driver.find_element(By.XPATH,"//input[@id='BE_flight_arrival_city']")

        time.sleep(2)
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
        time.sleep(2)


        all_dates= driver.find_elements(By.XPATH,"//div[@id='monthWrapper']// tbody//td[@class!='inActiveTD ']")
        for date in all_dates:
            if date.get_attribute("data-date")== "10/04/2023":
                date.click()
                break
        time.sleep(4)
A1 = Auto_Sugg ()
A1.autosuggedtion()
