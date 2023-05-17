from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

s = Service("ChromeDriverManager().install()")
driver = webdriver.Chrome(service=s)
driver.get("https://demos.telerik.com/kendo-ui/dragdrop/index")
driver.maximize_window()
sleep(3)

driver.find_element(By.XPATH, "//*[@id='onetrust-pc-btn-handler']").send_keys(Keys.ENTER)
driver.find_element(By.XPATH, "//*[@id='accept-recommended-btn-handler']").send_keys(Keys.ENTER)

sleep(2)
draggable = driver.find_element(By.ID, "draggable")
drop_target = driver.find_element(By.ID, "droptarget")

webdriver.ActionChains(driver).drag_and_drop(draggable, drop_target).perform()

sleep(5)

