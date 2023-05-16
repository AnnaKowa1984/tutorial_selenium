from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("ChromeDriverManager().install()")
driver = webdriver.Chrome(service=s)
driver.get("file:///C:/Users/Ania/PycharmProjects/zasoby/Test.html")
driver.maximize_window()
sleep(3)
driver.find_element(By.ID, "newPage").click()
print(driver.title)
sleep(2)
# lokalizujemy nasze obecne okno - jak ono się nazywa
current_window_name = driver.current_window_handle
window_names = driver.window_handles # pobieramy wszystkie okna które są dostepne dla drivera

# teraz będziemy iterować po tych wszystkich oknach
for window in window_names:
    if window != current_window_name:  # jeśli któreś z okien jest różne od tego pierwotnego, to chcemy się do niego przełaczyć
        driver.switch_to.window(window)

print(driver.title)
sleep(3)

# teraz ponownie wracamy do strony testowej żeby na niej pracować
driver.switch_to.window(current_window_name)
print(driver.title)
sleep(5)