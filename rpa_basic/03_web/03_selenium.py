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

# driver.get("http://naver.com") # 실행할 페이지의 url 입력

# # driver.back() # 뒤로가기
# # driver.forward() # 앞으로가기
# # driver.refresh() # 새로고침

# # a_containing_span_with_text_cafe = driver.find_element(By.XPATH, "//a[span/text()=\"카페\"]") # 카페에 해당하는 엘리먼트 찾기
# # print(a_containing_span_with_text_cafe) 카페에 해당하는 요소 출력
# # a_containing_span_with_text_cafe.click() 카페 부분 클릭


# search_elem = driver.find_element(By.ID, "query") # 검색창에 해당하는 엘리먼트 찾기
# # print(search_elem) # 검색창에 해당하는 요소 출력
# search_elem.send_keys("나도코딩") # 검색창에 "나도코딩" 이라고 입력
# search_elem.send_keys(Keys.ENTER) # enter 키 입력

# # a_elem = driver.find_element(By.TAG_NAME, "a") # a 태그에 해당하는 '첫' 엘리먼트를 가져옴
# # print(a_elem.get_attribute("href"))

# a_elems = driver.find_elements(By.TAG_NAME, "a") # a 태그에 해당하는 '모든' 엘리먼트를 가져옴
# for e in a_elems: # for문을 이용해 a_elems를 하나씩 지정해서 각각의 href 요소를 출력
#     print(e.get_attribute("href"))



driver.get("http://daum.net") # 페이지를 daum 으로 변경

search_elem = driver.find_element(By.NAME, "q") # 검색창의 엘리먼트 중 "name"="q" 를 이용
# search_elem.send_keys("나도코딩")
# search_elem.send_keys("나도코딩")
# search_elem.send_keys("나도코딩") # 글자가 연달아 입력 됨
# search_elem.clear() # 글자를 전부 지워줌

search_elem.send_keys("나도코딩")

find_icon_elem = driver.find_element(By.XPATH, "//*[@id=\"daumSearch\"]/fieldset/div/div/button[3]") # XPath를 이용하여 검색 아이콘 엘리먼트를 찾기
find_icon_elem.click()

# driver.save_screenshot("rpa_basic/03_web/daum.png") # 스크린샷을 찍고 지정한 경로로 저장

# print(driver.page_source) # 현재 html 문서의 소스 코드를 출력

# driver.close() # 현재 탭을 닫음
# driver.quit() # 현재 브라우저 전체를 닫음