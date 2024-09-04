from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set() # set -> {,,} -> unordered, unchangeable, dont allow duplicates. 
def getLinks(url):
    global pages
    html = urlopen("http://en.wikipedia.org" + url)
    bsObj