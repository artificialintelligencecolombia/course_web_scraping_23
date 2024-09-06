# Import libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup
# We need to handle possible errors
from urllib.error import HTTPError

url = "https://www.livingantioquia.com/" # Page could not be found on server | Server could not be found

try:
    html = urlopen(url)
except HTTPError as e:
    print(f"ERROR: {e}")
    # return null, break, or do some other "Plan B"
else:
    # program continues. Note: If you return or break in the
    # exception catch, you do not need to use the "else" statement
    html_bytes = html.read()
    bs_obj = BeautifulSoup(html_bytes, "html.parser")

print(bs_obj.h2)