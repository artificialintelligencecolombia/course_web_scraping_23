from urllib.request import urlopen # request to url
from bs4 import BeautifulSoup as bs4

url = ("http://www.pythonscraping.com/pages/warandpeace.html")

# Use urlopen to send a request to the specified URL.
html = urlopen(url)

# Third case is to covert the html content in a Bs object
bs_obj = bs4(html, 'html.parser') # Enables parsing and manipulation of the html structure

nameList = bs_obj.find_all("", {"class":"green"})
# prints all elements with class "green" -> NO MATTER THE TAG
# output: list -> []

text_list = []
# Extracting only the text of the list's elements
for name in nameList:
    text_list.append(name.get_text()) # List of tag strings
    # get_tex() method is one of the last steps to perform


# print(f"\n\nText list: {text_list}\n")
# print(f"Tags list (attrs):  {nameList}\n\n")

hs_list = bs_obj.find_all({"h1","h2"}) # Output: list!
first_h_tag = hs_list[0]

print(f"\nHs list: {hs_list}\n")
print(f"First tag: {first_h_tag.get_text()}")