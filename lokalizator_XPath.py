from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service(r"ChromeDriverManager().install")
driver = webdriver.Chrome(service=s)
driver.get("file:///C:/Users/Ania/PycharmProjects/zasoby/Test.html")
driver.maximize_window()
sleep(2)
driver.find_element(By.XPATH, "/html/body/table/tbody/tr/th")
driver.find_element(By.XPATH, "//tbody//th")
driver.find_element(By.XPATH, "//th")
driver.find_element(By.XPATH, "//th[text()='Month']")
driver.find_element(By.XPATH, "//button[@id='clickOnMe']")
driver.find_element(By.XPATH, "//input[@id='fname']/following-sibling::table")
driver.find_element(By.XPATH, "//input[@name='fname']/following-sibling::table")