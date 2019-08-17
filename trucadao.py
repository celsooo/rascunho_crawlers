# -*- coding: UTF-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
from openpyxl import Workbook

#Using OpenPyxl
book = Workbook()
sheet = book.active

num_page = input("How many pages do you wish to go through? ")#To do: insert error handling for page number greater than available
page = 1
for page in range(1, int(num_page)+1):
    my_url = "https://www.trucadao.com.br/venda/caminhoes-usados?page=" + str(page)
    print(my_url)
    uClient = urlopen(my_url)
    page_html = uClient.read()
    uClient.close()
    #html parsing
    page_soup = soup(page_html, "html.parser")
    #Data extraction
    preco = page_soup.find_all("h4",{"class":"col-sm-4 price"})
    titulo = page_soup.find_all("h2",{"class":"col-sm-8"})
    tipo = page_soup.find_all("span", {"itemprop":"audience"})
    marca = page_soup.find_all("span", {"itemprop":"name"})
    modelo = page_soup.find_all("span", {"itemprop":"model"})
    local = page_soup.find_all("span", {"itemprop":"addressLocality"})
    ### TO DO: find out link pattern to insert


    for row in range(40):
        rows = (
            (preco[row].text, titulo[row].text, tipo[row].text, marca[row].text, modelo[row].text, local[row].text)
        )
        sheet.append(rows)
        row = row + 1


book.save("trucadao.xlsx")



#Extração do link - REFINAR
#link2 = page_soup.find_all('a', {"class":"link-full-ad col-xs-12"})


