from bs4 import BeautifulSoup
import requests
import csv

sauce = requests.get('https://www.foodnetwork.com/restaurants/shows/diners-drive-ins-and-dives/a-z')
soup = BeautifulSoup(sauce.text, 'lxml')

name_list = []
address_list = []
desc_list = []

for article in soup.find_all('div', class_="m-MediaBlock o-Capsule__m-MediaBlock"):
        name = article.find('span', class_="m-MediaBlock__a-HeadlineText").text
        name_list.append(name)
        address = article.find("div", class_="m-Info__a-Address").text.lstrip()
        address_list.append(address)
        description = article.find('div', class_="m-MediaBlock__a-Description").text.lstrip()
        desc_list.append(description)
        if len(name_list) == 15:
            break

with open('food.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerows([name_list])
with open('food.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerows([desc_list])
with open('food.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerows([address_list])







