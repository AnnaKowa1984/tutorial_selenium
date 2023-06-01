from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os   # umożliwi pobranie odpowiedniej ścieżki

s = Service("ChromeDriverManager().install()")
driver = webdriver.Chrome(service=s)
driver.get("file:///C:/Users/Ania/PycharmProjects/zasoby/Test.html")
driver.maximize_window()
sleep(3)

paragraph = driver.find_element(By.TAG_NAME, "p")

if paragraph.is_displayed():
    print("Is displayed.")
    print(paragraph.text)
else:
    print("Is not displayed")
    print(paragraph.get_attribute("textContent"))

