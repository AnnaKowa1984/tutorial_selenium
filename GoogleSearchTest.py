

from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service

s = Service(r"C:\Users\Ania\PycharmProjects\tutorial_selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("http://google.com")
sleep(10)