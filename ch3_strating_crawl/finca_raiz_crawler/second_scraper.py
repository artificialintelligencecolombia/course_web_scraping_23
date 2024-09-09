# import libraries
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

def get_info(page_url):
    url = "https://www.fincaraiz.com.co/venta/fincas/san-vicente/antioquia"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
    req = Request(url, headers=headers)

    # Fetching and parsing html with bs4
    html = urlopen(req)
    bsObj = BeautifulSoup(html, "html.parser", from_encoding="utf-8")

    # Find all span tags regarding to property_price
    price_spans = bsObj.findAll("span", {"class": "ant-typography price heading heading-3 high"})
    # print(price_spans)

    # Find all span tags regarding to property description
    description_spans = bsObj.findAll("span", {"class": "body body-2 body-regular medium"})

    # print(description_spans)

    # Extract property descr. details
    strong_list = []
    for span in description_spans:
        strong_tags = span.findAll("strong")
        for strong in strong_tags:
            strong_list.append(strong.get_text())

    # print(strong_list)

    # Extract property prices
    property_price = []
    for span in price_spans:
        strong_tag = span.find("strong")
        # print(strong_tag)

        if strong_tag:
            property_price.append(strong_tag.get_text(strip=True))
    
    return property_price

list = get_info("")
# print(list)