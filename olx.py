from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
from openpyxl import Workbook

#Using OpenPyxl
book = Workbook()
sheet = book.active


num_page = input("How many pages do you wish to go through?")#To do: insert error handling for page number greater than available

for page in range(1, int(num_page)+1):
    my_url = "https://sp.olx.com.br/vale-do-paraiba-e-litoral-norte/vale-do-paraiba/sao-jose-dos-campos/celulares?o="+str(page)
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
    print(my_url)

    for row in range(40):
        rows = (
            (title[row].text, price[row].text, region[row].text, link[row].get('href'), date[row].text)
        )
        sheet.append(rows)


book.save("olx.xlsx")


'''
for product in range(3):
    print(price[product].text)
    print(title[product].text)
    print(region[product].text)
    print(date[product].text)
    print(link[product].get('href'))'''