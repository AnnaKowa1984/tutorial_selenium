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
print(driver.find_element(By.TAG_NAME, "p").get_attribute("textContent"))
# żeby wyświetlić tekst zawarty w elemencie, który jest ukryty korzystamy z metody: get_attribute i jako parametr podajemy "textContent"
driver.find_element(By.ID, "fname").send_keys("Ania")
print("Element text: " + driver.find_element(By.ID, "fname").get_attribute("value"))
# żeby wyświetlić tekst zawarty w inpucie, korzystamy z metody: get_attribute i jako parametr podajemy "value"
sleep(5)
