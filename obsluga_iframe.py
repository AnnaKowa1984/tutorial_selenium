from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# iframe - specjalny tah html, który umozliwia umieszczenie strony wewnatrz takiego tagu (strona wewnatrz strony)

s = Service("ChromeDriverManager().install()")
driver = webdriver.Chrome(service=s)
driver.get("file:///C:/Users/Ania/PycharmProjects/zasoby/iFrameTest.html")
driver.maximize_window()

# sprawdzamy jaka wartość tekstową ma nagłówek h1
print(driver.find_element(By.TAG_NAME, "h1").text)

#przelaczamy sie do iframe'a
driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))
print(driver.find_element(By.TAG_NAME, "h1").text)

# wracamy do pierwotnego frame'a
driver.switch_to.default_content()      # powrót do domyślnego contentu - do pierwszej, nadrzędnej strony
print(driver.find_element(By.TAG_NAME, "h1").text)
sleep(5)

