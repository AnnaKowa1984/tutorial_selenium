# jeżeli pole tekstowe jest enable to możemy wprowadzic do niego wartość,
# jeżeli nie jest, to nie możemy nic w nim zrobić - pole jest wyszarzone


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

first_name_input = driver.find_element(By.NAME, "fname")

if first_name_input.is_enabled():
    # first_name_input.click()
    first_name_input.send_keys("Tomek")
else:
    print("Element nie jest dostepny.")


sleep(2)