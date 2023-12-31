from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time

options = ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
# driver.maximize_window() # 창 최대화

driver.get('https://www.w3schools.com/')

first_name = "나도"
last_name = "코딩"
country = "Canada"
subject = "퀴즈 완료하였습니다."

driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div/div[1]/a[1]').click()
driver.find_element(By.XPATH, '//*[@id="subtopnav"]/a[8]').click()
driver.find_element(By.XPATH, '//*[@id="leftmenuinnerinner"]/a[120]').click()
driver.find_element(By.XPATH, '//*[@id="fname"]').send_keys(first_name)
driver.find_element(By.XPATH, '//*[@id="lname"]').send_keys(last_name)
driver.find_element(By.XPATH, f'//*[@id="country"]/option[text()="{country}"]').click()
driver.find_element(By.XPATH, '//*[@id="main"]/div[3]/textarea').send_keys(subject)

time.sleep(5)

driver.find_element(By.XPATH, '//*[@id="main"]/div[3]/a').click()

time.sleep(5)

driver.quit()