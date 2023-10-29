from openpyxl import load_workbook
wb = load_workbook("rpa_basic\\01_excel\\sample.xlsx")
ws = wb.active

# ws.delete_rows(8) # 8번째 행에 있는 7번 학생 데이터 삭제
# ws.delete_rows(8, 3) # 8번째 행부터 총 3줄 삭제
# wb.save("rpa_basic\\01_excel\\sample_delete_row.xlsx")

# ws.delete_cols(2) # 2번째 열 (B) 삭제
ws.delete_cols(2, 2) # 2번째 열로부터 총 2개 열 삭제
wb.save("rpa_basic\\01_excel\\sample_delete_col.xlsx")