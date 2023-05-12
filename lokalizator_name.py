from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service(r"ChromeDriveManager().install()")
driver = webdriver.Chrome(service=s)
driver.get("file:///C:/Users/Ania/PycharmProjects/zasoby/Test.html")
sleep(2)
driver.maximize_window()
sleep(2)
driver.find_element(By.ID, "clickOnMe")
driver.find_element(By.NAME, "fname")
sleep(5)