import pyautogui
import pyperclip

pyautogui.hotkey("winleft", "r")
pyperclip.copy("mspaint")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

pyautogui.sleep(1)

w = pyautogui.getWindowsWithTitle("그림판")[0]

if w.isActive == False: # 현재 활성화가 되지 않았다면
    w.activate() # 활성화 (맨 앞으로 가져오기)

if w.isMaximized == False: # 현재 최대화가 되지 않았다면
    w.maximize() # 최대화

pyautogui.sleep(1)

pyautogui.click(1260, 800, duration=0.25) # 그림판에 텍스트만 있으면 저장 여부를 묻지 않아서 넣은 부분

txt_btn = pyautogui.locateOnScreen("rpa_basic/02_desktop/txt_btn.png")
pyautogui.click(txt_btn, duration=0.25)

pyautogui.click(1260, 800, duration=0.25)

pyperclip.copy("참 잘했어요")
pyautogui.hotkey("ctrl", "v")

pyautogui.sleep(5)

w.restore()
pyautogui.sleep(1) 
w.close()

pyautogui.sleep(1)

dont_save_btn = pyautogui.locateOnScreen("rpa_basic/02_desktop/dont_save_btn.png")
pyautogui.click(dont_save_btn, duration=0.25)