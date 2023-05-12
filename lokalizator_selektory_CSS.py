from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service(r"ChromeDriveManager().install()")
driver = webdriver.Chrome(service=s)
driver.get("file:///C:/Users/Ania/PycharmProjects/zasoby/Test.html")
driver.maximize_window()
sleep(2)
driver.find_element(By.CSS_SELECTOR, "a")
driver.find_element(By.CSS_SELECTOR, "img#smileImage")
driver.find_element(By.CSS_SELECTOR, "p.topSecret")
print(driver.find_element(By.CSS_SELECTOR, "th:first-child").text)
print(driver.find_element(By.CSS_SELECTOR, "th:last-child").text)
sleep(3)