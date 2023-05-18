from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os   # umożliwi pobranie odpowiedniej ścieżki

s = Service("ChromeDriverManager().install()")
driver = webdriver.Chrome(service=s)
driver.get("file:///C:/Users/Ania/PycharmProjects/zasoby/FileUpload.html")
driver.maximize_window()
sleep(3)

upload_input = driver.find_element(By.ID, "myFile")
sleep(2)

path = os.path.abspath("upload.txt")

upload_input.send_keys(path)  # wysyłamy ścieżkę do inputa za pomocą send_keys

sleep(5)