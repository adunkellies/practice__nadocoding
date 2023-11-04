from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
# driver.maximize_window() # 창 최대화

driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_checkbox")

driver.switch_to.frame("iframeResult")

elem = driver.find_element(By.XPATH, "//*[@id=\"vehicle1\"]")

time.sleep(5)

if elem.is_selected() == False:
    print("선택 안되어 있으므로 선택")
    elem.click()
else:
    print("선택 되어 있으므로 아무것도 안함")

time.sleep(5)
driver.quit()