from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Open a site using `driver`

driver.get("https://google.com")

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located(By.CLASS_NAME, "gLFyf")
) # After 5 Sec the element we can't able find the element means crash the program or go head for next move


# Find the `Seatch Element`
input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.clear() # Clear the field fiels instead of override
input_element.send_keys("tech with tim" + Keys.ENTER)


time.sleep(10)

driver.quit()