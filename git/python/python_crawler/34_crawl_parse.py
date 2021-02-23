import requests
from bs4 import BeautifulSoup

#crawl -> 데이터 가져오기
#parse -> 정보 뽑아내기 price

def crawl(url):
    data = requests.get(url)
    print(data)
    return data.content

def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    #print(bsObj) #대한민국 -> 강남구 -> 서초동 -> 김씨
    noToday = bsObj.find("p", {"class": "no_today"})
    blind = noToday.find("span", {"class": "blind"})
    price = blind.text
    return price

#g o f(x) -> parse o crawl(url)
url = "https://finance.naver.com/item/main.nhn?code=068270"
pageString = crawl(url)
price = parse(pageString)
print(price)