# to_list = ["adunkellies@gmail.com", "adunkellies@gmail.com", "adunkellies@gmail.com"]
# msg = ":".join(to_list)
# print(msg)

import time
print(time.strftime('%d-%b-%Y')) # 현재 날짜를 일-월-연도

import datetime
dt = datetime.datetime.strptime("2002-11-15", "%Y-%m-%d")
print(type(dt))
print(dt.strftime('%d-%b-%Y'))