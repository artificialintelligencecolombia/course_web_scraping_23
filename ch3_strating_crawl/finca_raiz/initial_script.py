from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()

def getLinks(pageUrl):
    global pages
    html = urlopen("https://www.fincaraiz.com.co/venta/fincas/san-vicente/antioquia" + pageUrl) # SERVER REFUSES TO AUTHORIZE THE REQUEST. -> Solution: headers = {user_agent: mozilla}
    bsObj = BeautifulSoup(html)
    try:
        # print(bsObj.h1.get_text())
        print(bsObj.findAll("span", {"class": "ant-typography price heading heading-3 high"}))
        # print(bsObj.find(id="ca-edit").find("span").find("a").attrs['href'])
    except AttributeError:
        print("This page is missing something! No worries though!")

#    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
#        if 'href' in link.attrs:
#            if link.attrs['href'] not in pages:
#                #We have encountered a new page
#                newPage = link.attrs['href']
#                print("----------------\n"+newPage)
#                pages.add(newPage)
#                getLinks(newPage)
#                getLinks("")

getLinks("")

# An HTTP 403 error (Forbidden) occurs when the server understands the request but refuses to authorize it. This can happen for several reasons, such as:

# The server detects the request is from a bot (as in the second script without a User-Agent).