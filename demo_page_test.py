from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


s = Service(r"ChromeDriverManager().install()")
driver = webdriver.Chrome(service=s)
driver.get("file:///C:/Users/Ania/PycharmProjects/zasoby/Test.html")
driver.maximize_window()
driver.find_element(By.ID,"newPage").click()
sleep(5)
# driver.quit()   # zamyka wszystkie okna
driver.close()  # zamyka tylko to okno, na którym było dziłanie
sleep(10)