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

driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_option")

driver.switch_to.frame("iframeResult")

# # //*[@id="cars"]/option[4]   # cars 에 해당하는 element 를 찾고, 드롭다운 내부에 있는 4번째 옵션을 선택
# elem = driver.find_element(By.XPATH, "//*[@id=\"cars\"]/option[4]")
# # option[1] : 첫번째 항목
# # option[2] : 두번째 항목
# # ...
# elem.click()

# # 완전히 일치하는 텍스트 값을 통해서 선택하는 방법
# # 옵션 중에서 텍스트가 Audi 인 항목을 선택
# elem = driver.find_element(By.XPATH, "//*[@id=\"cars\"]/option[text()=\"Audi\"]")
# elem.click()

# 텍스트 값이 부분 일치하는 항목 선택하는 방법
elem = driver.find_element(By.XPATH, "//*[@id=\"cars\"]/option[contains(text(), \"Au\")]")
elem.click()

time.sleep(5)

driver.quit()