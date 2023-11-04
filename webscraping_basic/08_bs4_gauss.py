import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=799793"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
with open("webscraping_basic//08_bs4_gauss_html.html", "w", encoding="utf-8") as f:
    f.write(soup.prettify())

# srcs = soup.find_all("script", attrs={"type":"text/javascript"})
# # src1 = srcs[0]["src"]
# # print(src1)

# for src_info in srcs:
#     src = src_info["src"]
#     print(src)

scripts = soup.find_all("script")
for script in scripts:
    script_txt = script.get_text()
    print(script_txt)