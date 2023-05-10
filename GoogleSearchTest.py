

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep


s = Service(r"C:\Users\Ania\PycharmProjects\tutorial_selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("http://google.com")
sleep(10)