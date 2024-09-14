# import libraries
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import pandas as pd

# -------------- MAKING REQUEST -> CREATE THE BSOBJECT --------------------------------
url = "https://www.metrocuadrado.com/apartaestudio-apartamento-casa-oficina-local-bodega-lote-finca-edificio-de-oficinas-consultorio-edificio-de-apartamentos/venta/rionegro/?search=form"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
req = Request(url, headers=headers)

# Fetching and parsing html with bs4
html = urlopen(req)
bsObj = BeautifulSoup(html, "html.parser", from_encoding="utf-8")
# print(bsObj)

# --------------------FINDING THE LIST OF ELEMENTS
 # Find all span tags regarding to property_price
price_p = bsObj.findAll("div", {"class": "sc-dxgOiQ BSoGx card-title"})
print(price_p)

# Extract property prices
property_price = []
for p in price_p:
    property_price.append(p.get_text())
    #print(strong_tag)
    
# -------------- CREATION OF DATAFRAME, APPENDING COLUMNS
df = pd.DataFrame(property_price,columns=['price'])

print(df)