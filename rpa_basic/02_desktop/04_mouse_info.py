import pyautogui
# pyautogui.FAILSAFE = False
pyautogui.PAUSE = 1 # 모든 동작에 1초씩 sleep 적용
# pyautogui.mouseInfo() # pyautogui 에서 제공하는 마우스 위치 정보 프로그램

for i in range(5):
    pyautogui.move(100, 100)