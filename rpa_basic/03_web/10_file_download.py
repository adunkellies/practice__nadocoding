from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time

options = ChromeOptions()
# options.add_experimental_option("detach", True)  # 다운로드 경로를 지정하려면 아래와 같이 add_experimental_option 를 수정
options.add_experimental_option('prefs', {'download.default_directory':r'C:\coding\practice\nadocoding\rpa_basic\03_web'})
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
# driver.maximize_window() # 창 최대화

driver.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_a_download')

driver.switch_to.frame('iframeResult')

# download 링크 클릭
elem = driver.find_element(By.XPATH, '/html/body/p[2]/a')
elem.click()

time.sleep(5)
driver.quit()