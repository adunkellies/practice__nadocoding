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
driver.maximize_window() # 창 최대화

driver.get('https://www.w3schools.com/tags/att_input_type_radio.asp')
curr_handle = driver.current_window_handle
print(curr_handle) # 현재 윈도우 핸들 정보

# Try it yourself
driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/a').click()

handles = driver.window_handles # 모든 핸들 정보
for handle in handles:
    print(handle) # 각 핸들 정보
    driver.switch_to.window(handle) # 각 핸들로 이동해서
    print(driver.title) # 출력해보면 현재 핸들 (브라우저) 의 제목 표시
    print()

# 새로 이동된 브라우저에서 뭔가 자동화 작업을 수행..

# 그 브라우저를 종료
print("현재 핸들 닫기")
driver.close()

# 이전 핸들로 돌아오기
print("처음 핸들로 돌아오기")
driver.switch_to.window(curr_handle)

print(driver.title) # HTML input type="radio"

# 브라우저 컨트롤이 가능한지 확인
time.sleep(5)
driver.get('http://daum.net')

time.sleep(5)
driver.quit()