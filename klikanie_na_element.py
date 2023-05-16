from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("ChromeDriverManager().install()")
driver = webdriver.Chrome(service=s)
driver.get("file:///C:/Users/Ania/PycharmProjects/zasoby/Test.html")
driver.maximize_window()
sleep(3)
# driver.find_element(By.ID, "clickOnMe").click()
click_me_button = driver.find_element(By.ID, "clickOnMe")
click_me_button.click()
sleep(3)