# import required libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

# Its a common practice to store the url in a variable
url = "http://pythonscraping.com/pages/page1.html"

# Use urlopen to send a request to the specified URL.
html = urlopen(url)

# The object 'html' is an HTTPResponse object from which you
# can read the content.
# Read the content of the response FIRST and decode it to convert from bytes to a string.
html_bytes = html.read()
html_text = html_bytes.decode('utf-8')

# Third case is to covert the html content in a Bs object
bs_obj = bs(html_bytes, 'html.parser') # Enables parsing and manipulation of the html structure

# Assuming 'html_bytes' contains the bytes and 'html_text' contains the decoded string
with open("scrape_test_comparison.txt", "w") as file1:
    file1.write(f"The html.read() prints bytes, not human-readable HTML: \n {html_bytes}\n\n")
    file1.write(f"The html.read().decode('utf-8') prints a human-readable HTML string: \n {html_text}\n\n")
    file1.write(f"The beautiful soup object is: \n {bs_obj}\n\n")
    # Write explanations to the file.
    file1.write("- html.read() retrieves the HTML content as bytes.\n")
    file1.write("- UTF-8 decoding converts these bytes into a human-readable string.\n")
    file1.write("- A BeautifulSoup object is used to parse and manipulate the HTML, allowing for easy iteration and modification.\n")
