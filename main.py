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

# Find the `Seatch Element`
input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.clear() # Clear the field fiels instead of override
input_element.send_keys("tech with tim" + Keys.ENTER)

time.sleep(10)

driver.quit()