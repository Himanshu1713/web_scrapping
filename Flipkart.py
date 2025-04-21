# first we import all the libraries which is required to do web scrapping

import pandas as pd 
import requests
from bs4 import BeautifulSoup

# create the empty list to store the scrapped data 
product_name = []
price = []
original_price = []
description = []
reviews = []

# paste the url of the website of which we are going to scrap the data and create a for loop to fetch mutltiple page of the data.

for i in range(2,20):

# url of the website from where we can fetch the data 
    url = "https://www.flipkart.com/search?q=mobile+under+25000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=1"


# passing the http request 

    r = requests.get(url)
    # print(r)

# if you got the response 200 mean our http request was successful. 

# soup containg all the data into init.
    soup = BeautifulSoup(r.text , 'html.parser')
    

# we can create the box variable and store the all the usefull data in it and for further use.
# another reason is for creating this is to retrive the only data which inside the page.  
     
    box = soup.find("div", class_ = "DOjaWF gdgoEp")

# retrive the product name  and with the help of loops data added to the product_name list 

    pname = box.find_all("div" ,class_="KzDlHZ" )
 
    for p in pname:
        product_name.append(p.text.strip())

# retrive the price of the product and with the help of loops data added to the Price list   

    pc = box.find_all("div" , class_="Nx9bqj _4b5DiR")

    for pr in pc:
        price.append(pr.text.strip())

# retrive the Original price of the data without any discount and data added to the original_price

    orp = box.find_all("div" , class_ ="yRaY8j ZYYwLA")

    for op in orp:
        original_price.append(op.text.strip())

# retrive the reviews of the product and with the help of loops data added to the reviews list 
    rev = box.find_all("div",class_="XQDdHH")
    
    for re in rev:
        reviews.append(re.text)
    

# retrive the full description of the product and with the help of loops data added to the Description list

    desc = box.find_all("div" , class_ = "_6NESgJ")


    for de in desc :
        description.append(de.text)
        
# here we can do small check that all the list have data and quantity of data will be equal otherwise dataframe function gives an error

print(len(product_name))
print(len(price))
print(len(reviews))
print(len(description))
print(len(original_price))

# here come's the last second step of this assignment which is creating the data frame using pandas function 
df = pd.DataFrame({"Product Name":product_name,"Price":price,"Ratings":reviews,"Original Price":original_price,"Description":description})

# and the last step of this assignment is that we can make a csv file of the data for further cleaning and assesment process.
df.to_csv("E:/scrapping/flipkart.csv")