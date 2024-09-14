# import libraries
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import pandas as pd

# -------------- MAKING REQUEST -> CREATE THE BSOBJECT --------------------------------
url = "https://www.fincaraiz.com.co/venta/casas-y-apartamentos-y-fincas-y-cabanas-y-casas-lotes/rionegro/antioquia"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
req = Request(url, headers=headers)

# Fetching and parsing html with bs4
html = urlopen(req)
bsObj = BeautifulSoup(html, "html.parser", from_encoding="utf-8")

def get_info(page_url):
    
    # --------------------FINDING THE LIST OF ELEMENTS
    # Find all span tags regarding to property_price
    price_spans = bsObj.findAll("span", {"class": "ant-typography price heading heading-3 high"})
    #print(price_spans)

    # Find all span tags regarding to property description
    description_spans = bsObj.findAll("span", {"class": "body body-2 body-regular medium"})
    #print(description_spans)

    # Fetch all strong tags related to the realtors
    realtor_strongs = bsObj.findAll("strong", {"class": "body body-2 high"})
    
    # Fetch all strong tags related to the city
    city_strongs = bsObj.findAll("strong", {"class": "lc-location body body-1 body-bold medium"})
    #print(city_strongs)
    
    # Fetch all span tags related to the type of property
    proptype_spans = bsObj.findAll("span", {"class": "lc-title body body-2 body-regular medium"})
    
    # ------------------ PYTHON LISTST -----------------------
    # Extract property descr. details
    data = []
    for span in description_spans:
        strong_tags = span.findAll("strong")
        for strong in strong_tags:
            data.append(strong.get_text())

    # Original list of data where the elements are mixed in sequence of 3 for each r.e.)
    # print(data)
    
    result = [data[i:i + 3] for i in range(0, len(data), 3)]
    # Use list comprehension to group every 3 consecutive elements into a sublist
    # Breakdown:
    # - data[i:i+3]: Slices the list into sublists of 3 elements (start at index i, end at i+3)
    # - range(0, len(data), 3): Iterates over the list with steps of 3 (i = 0, 3, 6, ...)

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
    
    # Create the list for the city where the property is located    
    city = [] 
    for strong in city_strongs:
        city.append(strong.get_text())
    
    # Create the column list for the type of property
    property_type = []
    for span in proptype_spans:
        property_type.append(span.get_text())    
        
    # -------------- CREATION OF DATAFRAME, APPENDING COLUMNS
    df = pd.DataFrame(result,columns=['Bedrooms', 'Bathromms','Area'])
    # Create a DataFrame with columns for Bedrooms, Bathrooms, and Size
    # print(strong_list)
    
    # Print the resulting list of sublists
    #print(df)

    df.insert(0, 'Price', property_price)
    df.insert(4, 'Realtor', realtor)
    df.insert(5, 'City', city)
    df.insert(6, 'Type', property_type)
    # Insert property_price, realtor and so on columns into df

    # Set display option to show all columns
    pd.set_option('display.max_columns', None)

    #print(property_price)
    #print(realtors)
    #print(df)
    return df

# ------------ LOOP FOR MULTIPLE SITES ------------

dataset = get_info("/pagina1")
print(dataset)
