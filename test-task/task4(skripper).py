from re import findall

from bs4 import BeautifulSoup
import requests

url='https://webscraper.io/test-sites/e-commerce/static/computers/laptops'
respone=requests.get(url)

soup=BeautifulSoup(respone.text,"html.parser")
num_page=soup.find_all('li',class_="page-item")
count_page=num_page[-2].find('a', class_="page-link").text
count_page_int=int(count_page)
note_list = []
for r in range(count_page_int):
    url = f'https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page={r+1}'
    respone = requests.get(url)
    soup = BeautifulSoup(respone.text, "html.parser")
    all_note= soup.find_all('div',class_='product-wrapper card-body')
    for i in all_note:
           title_note = i.find('a', class_="title").get('title')
           description_note = i.find('p', class_="description card-text").text
           note_list.append([title_note,description_note])

print(note_list)





