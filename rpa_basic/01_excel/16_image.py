from openpyxl import Workbook
from openpyxl.drawing.image import Image
wb = Workbook()
ws = wb.active

img = Image("rpa_basic\\01_excel\\img.png")

# C3 위치에 img.png 파일의 이미지를 삽입
ws.add_image(img, "C3")

wb.save("rpa_basic\\01_excel\\sample_image.xlsx")

# ImportError : You must install Pillow to fecth image....
# pip install Pillow