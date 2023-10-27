import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
with open("webscraping_basic//check_contents.html", "w", encoding="utf-8") as f:
    f.write(soup.prettify())
# print(soup.title)
# print(soup.title.get_text())
# print(soup.meta) # soup 객체에서 처음 발견되는 meta element 출력
# print(soup.meta.attrs) # meta element 의 속성 정보를 출력
# print(soup.meta["charset"]) # meta element 의 charset 속성 '값' 정보를 출력

# print(soup.find("meta", attrs={"content":"네이버 웹툰"})) # class="네이버 웹툰" 인 meta element 를 찾아줘 (첫번째를 반환)
# print(soup.find(attrs={"content":"네이버 웹툰"})) # class="네이버 웹툰" 인 어떤 element 를 찾아줘 (첫번째를 반환)

# print(soup.find("html", attrs={"lang":"ko"}))
html = soup.find("html", attrs={"lang":"ko"})
print(html.meta)