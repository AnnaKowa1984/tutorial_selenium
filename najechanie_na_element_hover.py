from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

s = Service("ChromeDriverManager().install()")
driver = webdriver.Chrome(service=s)
driver.get("https://www.w3schools.com/")
driver.maximize_window()
sleep(3)

driver.find_element(By.ID, "accept-choices").click()

sleep(2)

tutorials_element = driver.find_element(By.ID, "navbtn_tutorials")
webdriver.ActionChains(driver).move_to_element(tutorials_element).perform()

sleep(5)
