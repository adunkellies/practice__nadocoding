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
driver.maximize_window()

# 1. https://www.w3schools.com 접속 (URL 은 구글에서 w3schools 검색)
driver.get('https://www.w3schools.com/')

# 2. 화면 중간 LEARN HTML 클릭
driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div/div[1]/a[1]').click()

# 3. 상단 메뉴 중 HOW TO 클릭
driver.find_element(By.XPATH, '//*[@id="subtopnav"]/a[8]').click()

# 4. 좌측 메뉴 중 Contact Form 메뉴 클릭
# driver.find_element(By.XPATH, '//*[@id="leftmenuinnerinner"]/a[120]').click()

# 링크 텍스트로 비교 > Contact Form 이라는 2개 이상의 링크 텍스트가 있는 경우 실패
# driver.find_element(By.LINK_TEXT, 'Contact Form').click()

# 가장 좋은 방법 (텍스트 전체 일치 여부 비교)
driver.find_element(By.XPATH, '//*[@id="leftmenuinnerinner"]/a[text()="Contact Form"]').click()

# 일부 텍스트 비교하는 방법
# driver.find_element(By.XPATH, '//*[@id="leftmenuinnerinner"]/a[contains(text(), "Contact)]').click()

# 5. 입력란에 아래 값 입력
#   First Name : 나도
#   Last Name : 코딩
#   Country : Canada
#   Subject : 퀴즈 완료하였습니다.
#   * 위 값들은 변수로 미리 저장해두세요

first_name = "나도"
last_name = "코딩"
country = "Canada"
subject = "퀴즈 완료하였습니다."

driver.find_element(By.XPATH, '//*[@id="fname"]').send_keys(first_name)
driver.find_element(By.XPATH, '//*[@id="lname"]').send_keys(last_name)
driver.find_element(By.XPATH, f'//*[@id="country"]/option[text()="{country}"]').click()
driver.find_element(By.XPATH, '//*[@id="main"]/div[3]/textarea').send_keys(subject)

# 6. 5초 대기 후 Submit 버튼 클릭
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="main"]/div[3]/a').click()

# 7. 5초 대기 후 브라우저 종료
time.sleep(5)
driver.quit()