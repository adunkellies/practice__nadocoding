from tkinter import *

root = Tk()
root.title("제목 없음 - Windows 메모장")
root.geometry("320x240") # 가로 * 세로

menu = Menu(root)

# 파일 메뉴 명령
def file_open():
    with open('.\\mynote.txt', 'a+', encoding="UTF-8") as file:
        file.seek(0)
        s = file.read()
        txt.delete("1.0", END)
        txt.insert(END, s)

def file_save():
    with open('.\\mynote.txt', 'w', encoding="UTF-8") as file:
        file.write(txt.get("1.0", END))


# 파일 메뉴
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command=file_open)
menu_file.add_command(label="저장", command=file_save)
menu_file.add_separator()
menu_file.add_command(label="끝내기", command=root.quit)
menu.add_cascade(label="파일", menu=menu_file)

# 편집 메뉴
menu_edit = Menu(menu, tearoff=0)
menu.add_cascade(label="편집", menu=menu_edit)

# 서식 메뉴
menu_format = Menu(menu, tearoff=0)
menu.add_cascade(label="서식", menu=menu_format)

# 보기 메뉴
menu_view = Menu(menu, tearoff=0)
menu.add_cascade(label="보기", menu=menu_view)

# 도움말 메뉴
menu_help = Menu(menu, tearoff=0)
menu.add_cascade(label="도움말", menu=menu_help)


# 프레임
frame = Frame(root)
frame.pack(fill="both", expand=True)

# 스크롤 바
scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

# 메모장 부분
txt = Text(frame, yscrollcommand = scrollbar.set)
txt.pack(fill="both", expand=True)


# 메뉴 적용
root.config(menu=menu)
# 스크롤바 적용
scrollbar.config(command=txt.yview)
root.mainloop()