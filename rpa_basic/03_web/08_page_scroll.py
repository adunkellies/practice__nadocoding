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
driver.maximize_window() # 창 최대화

driver.get("https://shopping.naver.com/home")

# '무선마우스' 입력
elem = driver.find_element(By.XPATH, '//*[@id="gnb-gnb"]/div[2]/div/div[2]/div/div[2]/form/div[1]/div[1]/input')
elem.send_keys('무선마우스')

time.sleep(1)

elem.send_keys(Keys.ENTER) # 검색 버튼 클릭을 위해 Enter 처리

# 스크롤
# 지정한 위치로 스크롤 내리기
# 모니터 (해상도) 높이인 1080 위치로 스크롤 내리기
driver.execute_script('window.scrollTo(0, 1600)') # 2560 * 1600 (모니터 해상도)



time.sleep(5)
driver.quit()