
#crawling 크롤링 파싱 스크래핑
# craw() -> ㄷㅔ이터 받아오기
# parse() -> 받아온 데이터에서 필요한 정보 추출하기
# g o f(x) -> parse o crawl(url)
# crawl -> requests
# parse -> bs4

import requests

def crawl(url):
    data = requests.get(url)
    print(data)
    return data.content #렌더링

# crawl(url) -> data 받아오는 함수
url = "https://finance.naver.com/item/main.nhn?code=005930"
pageString = crawl(url)
print(pageString)