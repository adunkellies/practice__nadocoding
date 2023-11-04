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

driver.get('https://flight.naver.com/')

# 가는 날 클릭
driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[4]/div/div/div[2]/div[2]/button[1]').click()
time.sleep(1) # 시간 필요
driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[10]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[5]/button').click()
# 오는 날
time.sleep(1) # 시간 필요
driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[10]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[2]/td[3]/button').click()

# 도착 선택
time.sleep(1) # 시간 필요
driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[4]/div/div/div[2]/div[1]/button[2]/b').click()
# 검색창에 제주 입력
time.sleep(1) # 시간 필요
driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[10]/div[1]/div/input').send_keys('제주')
# 제주 선택
time.sleep(1) # 시간 필요
driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[10]/div[2]/section/div/a/div').click()

# 항공권 검색 클릭
time.sleep(1) # 시간 필요
driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[4]/div/div/div[2]/button').click()

# time.sleep(10)

try:
    elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[1]/div[6]/div/div[2]/div[2]/div/button')))
    print(elem)
except:
    print("실패했어요")

# # 첫 번째 결과 출력
# elem = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[6]/div/div[2]/div[2]/div/button')
# print(elem.text) # element 내에 있는 text 부분을 출력

time.sleep(5)
driver.quit()