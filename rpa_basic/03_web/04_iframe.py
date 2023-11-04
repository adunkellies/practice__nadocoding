# <html>
#   <body>
#       <iframe id="1">
#           <html>
#               <body>
#                   <div...>
#               </body>
#           </html>
#       </iframe>
#
#       <iframe id="2">
#           <html>
#               <body>
#                   <div...>
#               </body>
#           </html>
#       </iframe>
#   </body>
# </html>

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

driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio")

driver.switch_to.frame("iframeResult") # iframe의 id="iframeResult" 인 프레임으로 전환

elem = driver.find_element(By.XPATH, "//*[@id=\"html\"]") # //*[@id="html"]   # 성공

elem.click()

# driver.switch_to.default_content() # 상위로 빠져 나옴

# elem = driver.find_element(By.XPATH, "//*[@id=\"html\"]") # //*[@id="html"]   # 실패

# elem.click()

time.sleep(5) # 5초 대기

driver.quit()