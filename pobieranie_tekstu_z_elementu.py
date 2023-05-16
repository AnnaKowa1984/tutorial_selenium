from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

s = Service("ChromeDriverManager().install()")
driver = webdriver.Chrome(service=s)
driver.get("file:///C:/Users/Ania/PycharmProjects/zasoby/Test.html")
driver.maximize_window()
sleep(3)
driver.find_element(By.XPATH, "//input[@value='male']").click()    # wyszukujemy po strukturze imput i wartość atrybutu value jest równa male
sleep(1)
print(driver.find_element(By.XPATH, "//input[@value='male']").text)     # nic nie wydrukowało, bo nie ma tu tekstu wewnątrz tagu input
sleep(1)
print(driver.find_element(By.TAG_NAME, "h1").text)
sleep(1)
print(driver.find_element(By.ID, "clickOnMe").text)
sleep(1)
print(driver.find_element(By.TAG_NAME, "p").text)   # tekst zawarty w elemncie który jest ukryty nie zostal pobrany (hidden= )
sleep(5)
