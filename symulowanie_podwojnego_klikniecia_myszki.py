from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("ChromeDriverManager().install()")
driver = webdriver.Chrome(service=s)
driver.get("file:///C:/Users/Ania/PycharmProjects/zasoby/DoubleClick.html")
driver.maximize_window()
sleep(3)

button = driver.find_element(By.ID, "bottom")

webdriver.ActionChains(driver).double_click(button).perform()

sleep(5)