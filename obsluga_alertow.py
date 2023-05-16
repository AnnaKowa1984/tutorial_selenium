from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("ChromeDriverManager().install()")
driver = webdriver.Chrome(service=s)
driver.get("file:///C:/Users/Ania/PycharmProjects/zasoby/Test.html")
driver.maximize_window()
sleep(3)
driver.find_element(By.ID, "clickOnMe").click()
sleep(2)
driver.switch_to.alert.accept()     # alert został zaakceptowany
sleep(5)
driver.find_element(By.ID, "clickOnMe").click()
sleep(2)
driver.switch_to.alert.dismiss()    # alert został pominięty
sleep(5)