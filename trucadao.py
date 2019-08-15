# -*- coding: UTF-8 -*-
import bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import pandas as pd
my_url = "https://www.trucadao.com.br/venda/caminhoes-usados"

uClient = urlopen(my_url)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html, "html.parser")

#Extração dos dados
preco = page_soup.find_all("h4",{"class":"col-sm-4 price"})
titulo = page_soup.find_all("h2",{"class":"col-sm-8"})
tipo = page_soup.find_all("span", {"itemprop":"audience"})
marca = page_soup.find_all("span", {"itemprop":"name"})
modelo = page_soup.find_all("span", {"itemprop":"model"})
local = page_soup.find_all("span", {"itemprop":"addressLocality"})


#Extração do link - REFINAR
#link2 = page_soup.find_all('a', {"class":"link-full-ad col-xs-12"})


for a in range(40):
    print(titulo[a].text)
    print(preco[a].text)
    print(tipo[a].text)
    print(marca[a].text)
    print(modelo[a].text)
    print(local[a].text)