from re import findall

from bs4 import BeautifulSoup
import requests

url='https://webscraper.io/test-sites/e-commerce/static/computers/laptops'
respone=requests.get(url)

soup=BeautifulSoup(respone.text,"html.parser")
num_page=soup.find_all('li',class_="page-item")
c=num_page[-2].find('a', class_="page-link").text
t=int(c)
Note_list = []
for r in range(t):
    url = f'https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page={r+1}'
    respone = requests.get(url)
    soup = BeautifulSoup(respone.text, "html.parser")
    all_n= soup.find_all('div',class_='product-wrapper card-body')
    for i in all_n:
           a = i.find('a', class_="title").get('title')
           b = i.find('p', class_="description card-text").text
           Note_list.append([a,b])

print(Note_list)





