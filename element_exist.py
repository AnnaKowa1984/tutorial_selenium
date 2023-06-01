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

elements = driver.find_elements(By.TAG_NAME, "p")

# gdy damy find_element to wyskakuje błąd, bo nie ma takiego element na stronie
# gdy damy find_elements to ta metoda zwróci nam się lista i nie wyskoczy błąd, bo lista przybierze wartość 0

if len(elements) > 0:
    print("Element istnieje na stronie.")
else:
    print("Brak elementu na stronie.")


try:
    driver.find_element(By.TAG_NAME, "pawa")
    print("Element istnieje na stronie.")
# except NoSuchElementException:              <- To powinno działać.
except:
    print("Element nie istnieje.")

