from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://google.com")
driver.set_window_size(600, 600)
sleep(10)
