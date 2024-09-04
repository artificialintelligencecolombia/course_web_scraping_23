from urllib.request import urlopen # Fetch html content from a url 
from bs4 import BeautifulSoup # Parse and navigate html content
import datetime # Seeding random generator
import random # for select random links from the list of urls
import re # import regex to match specific patterns in text. 

# Get the current time as a datetime object
current_time = datetime.datetime.now()

# Convert the datetime to a timestamp (float) and then to an int
timestamp = int(current_time.timestamp())

# Use the integer timestamp as the seed
random.seed(timestamp)

# Function that takes a wikipedia url as input
def getLinks(article_url):
    # Fetch html content
    html = urlopen("http://en.wikipedia.org" + article_url)
    bsObj = BeautifulSoup(html, "html.parser") # parse the html content
    
    
    return bsObj.find("div", {"id" : "bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$"))
    # Find all the a tags within div->id:bodyContent container tag. Filter this selection with those that has 'href' ATTRIBUTE. Filter them with the REGEX pattern.
    
# Start the process by getting links from the Kevin Bacon Wikipedia page.
links = getLinks("/wiki/Kevin_Bacon")

# continue following links until there are no more links to follow.
while len(links) > 0:
    # select a random link from the list of links
    new_article = links[random.randint(0, len(links) - 1)].attrs["href"]
    
    #print the selected url
    #print(new_article)
    links = getLinks(new_article)
    print(links)
    
# The regex ^(/wiki/)((?!:).)*$ matches URLs that:
# 1. Start with /wiki/.
# 2. Do not contain a colon : (to exclude links to non-article pages like "Help:" or "Category:").

# OBJECTIVE:
# The script starts at Kevin Bacon's Wikipedia page, randomly follows a link to another Wikipedia page, prints the new page's URL, and continues this process indefinitely until it runs out of links to follow.