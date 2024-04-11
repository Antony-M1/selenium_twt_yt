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
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
) # After 5 Sec the element we can't able find the element means crash the program or go head for next move


# Find the `Seatch Element`
input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.clear() # Clear the field fiels instead of override
input_element.send_keys("tech with tim" + Keys.ENTER)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Tech With Tim"))
) # After 5 Sec the element we can't able find the element means crash the program or go head for next move


link = driver.find_element(By.PARTIAL_LINK_TEXT, "Tech With Tim") # Find the Link With Text & the `PARTIAL_LINK_TEXT` finds the if a text contains inside the `anchor` link if you want to check the exact text you can use the `LINK_TEXT`
link.click() # Click the Link



time.sleep(10)

driver.quit()