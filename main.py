from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Open a site using `driver`

driver.get("https://google.com")

time.sleep(10)

driver.quite()