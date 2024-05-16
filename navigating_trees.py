# Import required modules
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://www.pythonscraping.com/pages/page3.html"
html = urlopen(url)
bsObj = BeautifulSoup(html, 'html.parser')

for child in bsObj.find("table",{"id":"giftList"}).children:
    print(f"Table row: {child}\n")