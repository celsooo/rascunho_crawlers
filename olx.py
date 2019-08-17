from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
from openpyxl import Workbook

#Using OpenPyxl
#book = Workbook()
#sheet = book.active

my_url = "https://sp.olx.com.br/vale-do-paraiba-e-litoral-norte/vale-do-paraiba/sao-jose-dos-campos/celulares"
uClient = urlopen(my_url)
page_html = uClient.read()
uClient.close()
# html parsing
page_soup = soup(page_html, "html.parser")
# Data extraction
price = page_soup.find_all("p", {"class": "OLXad-list-price"})
title = page_soup.find_all("h2", {"class": "OLXad-list-title"})
region = page_soup.find_all("p", {"class": "text detail-region"})
date = page_soup.find_all("div", {"class": "col-4"})
link = page_soup.find_all("a", {"class": "OLXad-list-link"})



for product in range(3):
    print(price[product].text)
    print(title[product].text)
    print(region[product].text)
    print(date[product].text)
    print(link[product].get('href'))