from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Demo_fluenttwait:
    def fluentwaittime(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        text = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
        text.click()

        text.send_keys("New delhi")
        text.send_keys(Keys.ENTER)

        going_to = driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")

        going_to.click()
        going_to.send_keys("new")
        search_result = driver.find_elements(By.XPATH, "//div[@class='viewport']//div[1]/li")
        # print(len(Search_result))

        for results in search_result:
            print(results.text)
            if "New York (JFK)" in results.text:
                results.click()
                break
        wait = WebDriverWait(driver, 10, 2,ignored_exceptions=[ElementClickInterceptedException])

        # wait.until(EC.element_to_be_clickable((By.XPATH, "//label[@for='BE_flight_origin_date']")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_date']"))).click()

        # driver.find_element(By.XPATH, "//label[@for='BE_flight_origin_date']").click()
        all_dates = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='monthWrapper']// tbody//td[@class!='inActiveTD ']"))) \
            .find_elements(By.XPATH, "//div[@id='monthWrapper']// tbody//td[@class!='inActiveTD ']")

        # driver.find_elements(By.XPATH,"//div[@id='monthWrapper']// tbody//td[@class!='inActiveTD ']")
        for date in all_dates:
            if date.get_attribute("data-date") == "10/04/2023":
                date.click()
                break


obj1 = Demo_fluenttwait()
obj1.fluentwaittime()























