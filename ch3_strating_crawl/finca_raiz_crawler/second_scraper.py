# import libraries
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import pandas as pd

def get_info(page_url):
    url = "https://www.fincaraiz.com.co/venta/fincas/san-vicente/antioquia" + page_url
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
    req = Request(url, headers=headers)

    # Fetching and parsing html with bs4
    html = urlopen(req)
    bsObj = BeautifulSoup(html, "html.parser", from_encoding="utf-8")

    # Find all span tags regarding to property_price
    price_spans = bsObj.findAll("span", {"class": "ant-typography price heading heading-3 high"})
    #print(price_spans)

    # Find all span tags regarding to property description
    description_spans = bsObj.findAll("span", {"class": "body body-2 body-regular medium"})
    #print(description_spans)

    # Fetch all strong tags related to the realtors
    realtor_strongs = bsObj.findAll("strong", {"class": "body body-2 high"})
    

    # Extract property descr. details
    data = []
    for span in description_spans:
        strong_tags = span.findAll("strong")
        for strong in strong_tags:
            data.append(strong.get_text())

    # Original list of data where the elements are mixed in sequence of 3 for each r.e.)
    # print(data)

    # Use list comprehension to group every 3 consecutive elements into a sublist
    # Breakdown:
    # - data[i:i+3]: Slices the list into sublists of 3 elements (start at index i, end at i+3)
    # - range(0, len(data), 3): Iterates over the list with steps of 3 (i = 0, 3, 6, ...)
    result = [data[i:i + 3] for i in range(0, len(data), 3)]

    df = pd.DataFrame(result,columns=['Bedrooms', 'Bathromms','Area'])
    # Print the resulting list of sublists
    #print(df)

    # Create a DataFrame with columns for Bedrooms, Bathrooms, and Size
    # print(strong_list)

    # Extract property prices
    property_price = []
    for span in price_spans:
        strong_tag = span.find("strong")
        #print(strong_tag)

        if strong_tag:
            property_price.append(strong_tag.get_text(strip=True))

    realtor = []
    for strong in realtor_strongs:
        realtor.append(strong.get_text())

    # Insert property_price and realtor columns into df
    
    df.insert(0, 'Price', property_price)
    df.insert(4, 'Realtor', realtor)


    # Set display option to show all columns
    pd.set_option('display.max_columns', None)

    #print(property_price)
    #print(realtors)
    #print(df)
    return df

dataset = get_info("/pagina3")
print(dataset)
