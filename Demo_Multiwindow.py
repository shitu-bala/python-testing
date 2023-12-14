import  time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Multi_Windows:
    def open_multiplewindows(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        parent_handle=driver.current_window_handle
        print(parent_handle)
        driver.find_element(By.XPATH,"//a[@title='Free Cancellation']//img[@class='conta iner large-banner']").click()
        time.sleep(5)
        all_handler = driver.window_handles
        for handler in all_handler:
            if handler != parent_handle:
                driver.switch_to.window(handler)
                driver.find_element(By.XPATH,"//a[@id='booking_engine_holidays']").click()
                time.sleep(5)
                driver.close()


        driver.switch_to.window(parent_handle)
        driver.find_element(By.XPATH, "//a[@title='Free Cancellation']//img[@class='conta iner large-banner']").click()
        time.sleep(5)

a1= Multi_Windows()
a1.open_multiplewindows()
