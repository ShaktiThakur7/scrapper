import csv
import requests
from bs4 import BeautifulSoup
import json

#url of the website to scrap
url="http://books.toscrape.com/"


def scrape_books(url):
    response=requests.get(url)
    if response.status_code!=200:
        return
    

    #set encoding expicity to handle special character correctly
    response.encoding=response.apparent_encoding

    soup=BeautifulSoup(response.text,"html.parser")
    books=soup.find_all("article",class_="product_pod")
    list_book=[]
    for book in books:
        title=book.h3.a['title']
       
        price_text=book.find('p',class_='price_color').text
        currency=price_text[0]
        price=float(price_text[1:])
        print(title,price,currency)
        book_info = {
        "title": title,
        "price": price,
        "currency": currency
        }

        list_book.append(book_info)


        
    with open("books.json", "w", encoding="utf-8") as file:
        json.dump(list_book, file, indent=4, ensure_ascii=False)

 


   
    with open("books.csv","w",encoding="utf-8") as f:
        writer=csv.DictWriter(f,fieldnames=["title","price","currency"])
        writer.writeheader()
        writer.writerows(list_book)




scrape_books(url)
