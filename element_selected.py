from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os   # umożliwi pobranie odpowiedniej ścieżki

s = Service("ChromeDriverManager().install()")
driver = webdriver.Chrome(service=s)
driver.get("file:///C:/Users/Ania/PycharmProjects/zasoby/Test.html")
# driver.maximize_window()
sleep(3)

checkbox = driver.find_element(By.XPATH, "/html/body/label[2]/input[@type='checkbox']")
# checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox']")

checkbox.click()

if checkbox.is_selected():
    print("Wartość zaznaczona! Odznaczam!")
    checkbox.click()
else:
    print("Zaznaczam wartość.")
    checkbox.click()
