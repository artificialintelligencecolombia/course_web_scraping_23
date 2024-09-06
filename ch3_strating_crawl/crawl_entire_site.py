# import required libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re 

pages = set() # Stores the URLs of Wikipedia pages that have already been visited. 'set' ensures that each page is visited only once -> sets automatically handle duplicates.

def getLinks(page_url):
    global pages # Allows the function to modify the 'pages' set defined outside the function.

    html = urlopen("http://en.wikipedia.org"+ page_url) # Opens a speficied URL
    bs_obj = BeautifulSoup(html)
    
    for link in bs_obj.findAll("a", href=re.compile("^(/wiki/)")): # For each link, find all the urls -> /wiki/ word is required for the url. 
        if 'href' in link.attrs: # If the 'a' tag DOES have a 'href' attribute
            if link.attrs['href'] not in pages: # AND check IF the link has already been visited visited -> its not in the 'set()'. 
                # We have encountered a new page
                new_page = link.attrs['href']
                print(new_page) # prints THE URL OF THE NEW PAGE.
                pages.add(new_page) # add the new_page to the set for mark it as visited.
                getLinks(new_page) # Recursively calls the function to do the same on the new page. 
                
getLinks("") #getLinks(""): This kicks off the recursive crawling process starting from the main Wikipedia page -> "" empty str -> http://en.wikipedia.org
            