from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service


s = Service(r"ChromeDriverManager().install()")
driver = webdriver.Chrome(service=s)
driver.get("http://google.com")
driver.maximize_window()
sleep(10)