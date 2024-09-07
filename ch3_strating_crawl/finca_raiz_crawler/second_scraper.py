# import libraries
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

def get_info(page_url):
    url = "https://www.fincaraiz.com.co/venta/fincas/san-vicente/antioquia"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
    req = Request(url, headers=headers)

    html = urlopen(req)
    bsObj = BeautifulSoup(html, "html.parser")

    # Find all relevant span tags
    price_spans = bsObj.findAll("span", {"class": "ant-typography price heading heading-3 high"})
    # print(price_spans)

    prices = []
    for span in price_spans:
        strong_tag = span.find("strong")
        # print(strong_tag)

        if strong_tag:
            prices.append(strong_tag.get_text(strip=True))
    
    return prices

list = get_info("")
print(list)