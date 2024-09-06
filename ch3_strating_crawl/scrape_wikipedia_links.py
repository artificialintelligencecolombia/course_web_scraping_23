#!/usr/bin/env python3

from urllib.request import urlopen # Import urlopen to fetch HTML content from a URL.
from bs4 import BeautifulSoup # Parsing HTML content -> easier to navigate. 
import re  # Import re (regular expressions) to match specific patterns in text.

# Seed the random number generator with the current time.
# This ensures a different random path through Wikipedia articles every time the program is run.
random.seed(datetime.datetime.now())

#--------------------REQUEST AND PARSING OF TARGET WEBSITE --------------------
html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon") # Request to target URL.
#print(html) # html contains the HTML content.
#print(type(html)) 

# Parse the HTML content using BeautifulSoup.
bsObj = BeautifulSoup(html, "html.parser") # Object

# print(bsObj.prettify()) # Prints the parsed HTML content in a more readable format.

#-------------------------------SEARCH A TAGS WITH HREF ATTRIBUTE ----------------------------

# Find all <a> tags (links) within the div that has an id of "bodyContent".
# .findAll("a") retrieves all anchor tags.
# The "href" parameter ensures that we only find links starting with "/wiki/".
for link in bsObj.find("div", {"id": "bodyContent"}).findAll("a", 
         href=re.compile("^(/wiki/)((?!:).)*$")): # Explanation below:
    
    # Check if the link actually contains an "href" attribute (to avoid errors).
    if 'href' in link.attrs:
        # Print the value of the "href" attribute, which is the URL of the link.
        print(link.attrs['href'])
        


# Explanation of the regex:
    # ^(/wiki/) : This matches links that start with "/wiki/" (e.g., "/wiki/Python").
    # ((?!:).)* : This is a negative lookahead assertion that ensures the link doesn't contain a colon ":".
    #             The reason for this is to exclude non-article links like "/wiki/File:Example.jpg".
    # $ : End of the string.