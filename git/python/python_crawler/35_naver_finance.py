# crawl, parse

import requests
from bs4 import BeautifulSoup
def crawl(url):
    data = requests.get(url)
    print(data)
    return data.content

def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    noToday = bsObj.find("p", {"class": "no_today"})
    blind = noToday.find("span", {"class": "blind"})
    price = blind.text

    wrapCompany = bsObj.find("div", {"class": "wrap_company"})
    aTag = wrapCompany.find("a")
    name = aTag.text
    #print(name)

    description = bsObj.find("div", {"class": "description"})
    code = description.find("span", {"class": "code"})

    img = description.find("img")
    #print(img['alt'])
    category = img['alt']
    catEng = img['class']
    return {"price": price, "name": name, "code": code.text,
            "category": category, "catEng": catEng[0]}


url = "https://finance.naver.com/item/main.nhn?code=102940"
pageString = crawl(url)
companyInfo = parse(pageString)
print(companyInfo)
