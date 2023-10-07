import requests as rs
from bs4 import BeautifulSoup

url = 'http://wmii.uwm.edu.pl/kadra'
response = rs.get(url)

soup = BeautifulSoup(response.content, features='html.parser')
table = soup.find('table', class_="views-table cols-8").find('tbody')


# for row in table:
#     degree = row.find('td', class_='views-field views-field-degree').text.strip()
#     name = row.find('td', class_="views-field views-field-title active").text.strip()
#     phone = row.find('td', class_="views-field views-field-field-phone").text.strip()
#     print(degree, name, phone)

for i in table:
    email = i.find('td', "views-field views-field-field-email").text
    print(email)