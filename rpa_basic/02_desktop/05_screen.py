import pyautogui
# 스크린 샷 찍기
# img = pyautogui.screenshot()
# img.save("rpa_basic\\02_desktop\\screenshot.png") # 파일로 저장

# pyautogui.mouseInfo()
# 35,25 60,169,242 #3CA9F2

pixel = pyautogui.pixel(35, 25)
print(pixel)

# print(pyautogui.pixelMatchesColor(35, 25, (60,169,242)))
# print(pyautogui.pixelMatchesColor(35, 25, pixel))
print(pyautogui.pixelMatchesColor(35, 25, (60,169,243)))