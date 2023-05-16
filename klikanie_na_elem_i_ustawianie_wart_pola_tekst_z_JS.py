from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("ChromeDriverManager().install()")
driver = webdriver.Chrome(service=s)
driver.get("file:///C:/Users/Ania/PycharmProjects/zasoby/Test.html")
driver.maximize_window()
sleep(3)
# driver.execute_script("arguments[0].click();",driver.find_element(By.ID, "newPage"))        # klikniecie w JS
sleep(3)
wartosc = "Ania"
driver.execute_script("arguments[0].setAttribute('value', '" + wartosc +"')" , driver.find_element(By.ID, "fname"))
sleep(5)