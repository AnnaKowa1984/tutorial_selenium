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
auto_select = Select(driver.find_element(By.TAG_NAME, "select"))
auto_select.select_by_visible_text("Volvo")
sleep(3)
auto_select.select_by_value("saab")
sleep(3)
auto_select.select_by_index(2)
sleep(5)