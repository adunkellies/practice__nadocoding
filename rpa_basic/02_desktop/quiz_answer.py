import pyautogui
import sys
import pyperclip

pyautogui.hotkey("win", "r") # 단축키 : win + r 입력
pyautogui.write("mspaint")
pyautogui.press("enter") # 엔터 키 입력

# 그림판 나타날 때까지 2초 대기
pyautogui.sleep(2)

window = pyautogui.getWindowsWithTitle("제목 없음 - 그림판")[0] # 그림판 1개만 띄워져 있다고 가졍
if window.isMaximized == False:
    window.maximize() # 최대화

# 그림판에 텍스트만 있으면 저장 여부를 묻지 않아서 넣은 부분
pyautogui.click(1260, 800, duration=0.5)

# 글자 버튼 클릭
btn_text = pyautogui.locateOnScreen("rpa_basic/02_desktop/txt_btn.png")
if btn_text:
    pyautogui.click(btn_text, duration=0.5)
else:
    print("찾기 실패")
    sys.exit()

# # 흰 영역 클릭
# pyautogui.click(1260, 800, duration=0.5)

btn_brush = pyautogui.locateOnScreen("rpa_basic/02_desktop/btn_brush.png")
pyautogui.click(btn_brush.left + 400, btn_brush.top + 700, duration=0.5)

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")

my_write("참 잘했어요")

# 5초 대기
pyautogui.sleep(5)

# 프로그램 종료
window.close()
pyautogui.sleep(0.5)
pyautogui.press("n") # 저장하지 않음
