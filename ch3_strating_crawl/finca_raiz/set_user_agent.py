from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

pages = set()

def getLinks(pageUrl):
    global pages
    
    # Set a User-Agent header to mimic a browser request
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
    req = Request("https://www.fincaraiz.com.co/venta/fincas/san-vicente/antioquia", headers=headers)
    
    try:
        html = urlopen(req)
        bsObj = BeautifulSoup(html, "html.parser")
        print(bsObj.findAll("span", {"class": "ant-typography price heading heading-3 high"}))
    except HTTPError as e:
        print(f"HTTP Error: {e.code} {e.reason}")
    except AttributeError:
        print("This page is missing something! No worries though!")
    except Exception as e:
        print(f"An error occurred: {e}")

getLinks("")

