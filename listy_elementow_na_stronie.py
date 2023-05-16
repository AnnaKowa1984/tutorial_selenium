from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("ChromeDriverManager().install()")
driver = webdriver.Chrome(service=s)
driver.get("file:///C:/Users/Ania/PycharmProjects/zasoby/Test.html")
sleep(2)

elements_list_lenght = len(driver.find_elements(By.XPATH, "//th"))
print(elements_list_lenght)

# metoda find_element zwróci TYLKO pierwszy element z listy
# żeby zwrócić wszystkie elementy należy użyć metody find_elements