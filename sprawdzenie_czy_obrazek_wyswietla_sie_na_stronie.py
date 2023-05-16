from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("ChromeDriverManager().install()")
driver = webdriver.Chrome(service=s)
driver.get("file:///C:/Users/Ania/PycharmProjects/zasoby/Test.html")
driver.maximize_window()
sleep(3)
print("The height of web element is: " + str(driver.find_element(By.ID, "smileImage").size.get("height")))   # wypisujemy wysokość naszego web elementu
sleep(5)
print("The natural height of web element is: " + str(driver.find_element(By.ID, "smileImage").get_attribute("naturalHeight")))  # rekomendowany sposób