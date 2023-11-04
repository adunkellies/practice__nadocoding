import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
with open("webscraping_basic//07_bs4_webtoons_html.html", "w", encoding="utf-8") as f:
    f.write(soup.prettify())

# tag가 script인것 중 type="text/javascript" 전부 가져오기
srcs = soup.find_all("script", attrs={"type":"text/javascript"})
# 가져온 것들의 src 값 반환
for src in srcs:
    print(src["src"])