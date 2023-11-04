from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time



options = ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
driver.maximize_window() # 창 최대화

driver.get("https://www.w3schools.com/html/")

time.sleep(5)

# 특정 영역 스크롤
elem = driver.find_element(By.XPATH, '//*[@id="leftmenuinnerinner"]/a[66]')

# 방법 1 : ActionChain
# actions = ActionChains(driver)
# actions.move_to_element(elem).perform()

# 방법 2 : 좌표 정보 이용
# xy = elem.location_once_scrolled_into_view # 함수가 아닌 변수이므로 () 사용하지 않음
# print("type : ", type(xy)) # dict
# print("value : ", xy)

elem.click()

time.sleep(5)
driver.quit()