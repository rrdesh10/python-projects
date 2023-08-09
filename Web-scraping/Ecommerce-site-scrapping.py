from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import csv

# url for scrapping 
site_url = "https://www.flipkart.com/search?q=oneplus+mobiles&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_15_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_15_na_na_na&as-pos=1&as-type=RECENT&suggestionId=oneplus+mobiles%7CMobiles&requestId=fce52697-f0d5-4562-90ee-a9a0d614a39e&as-searchtext=oneplus%20mobiles"

# open the url and read
url_client = urlopen(site_url)
page_html = url_client.read()
url_client.close()

# create beautiful soup variable
page_soup = soup(page_html, features="html.parser")

# find divs from html 
containers = page_soup.find_all('div', {'class':'_3pLy-c row'})

#  Create CSV file to store data
with open("python-projects/Web-scraping/Oneplus-mobiles.csv", 'w', encoding='utf-8') as f:
    writer = csv.writer(f)
    headers = ["Product_Name" , "Price", "Rating"]
    writer.writerow(headers)

    # itreate over the containers and get all details  
    for container in containers:
        
        name_container = container.findAll("div", {"class": "_4rR01T"})
        name = name_container[0].text
    
        price_container = container.findAll("div", {"class": "_30jeq3 _1_WHN1"})
        price = price_container[0].text
        
        
        rating_container = container.findAll("div", {"class": "gUuXy-"})
        rating = rating_container[0].text
        rating = rating[0:3] + " "+ rating[3:]
        
        # write the data to csv file
        row = [[name, price, rating]]
        writer.writerows(row)





