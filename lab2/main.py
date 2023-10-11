# import json
import requests
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup


# url = 'https://api.gios.gov.pl/pjp-api/rest/station/findAll'
# response = requests.get(url)
#
# print(response.content)
#
# response.content.decode('utf-8')
#
# content = response.content.decode('utf-8')
# parsed_content = json.loads(content)
#
# print(type(response.content), type(content), type(parsed_content))
#
# print(parsed_content)
#
# station_id = 877
# url = f'https://api.gios.gov.pl/pjp-api/rest/station/sensors/{station_id}'
# response = requests.get(url)
#
# if response.status_code != 200:
#   exit()
#
# stations = json.loads(response.content.decode('utf-8'))
#
# print(stations)
#
# sensor_id = 5766
# url = f'https://api.gios.gov.pl/pjp-api/rest/data/getData/{sensor_id}'
# response = requests.get(url)
#
# if response.status_code != 200:
#   assert False

# data = json.loads(response.content.decode('utf-8'))
# value = data['values'][0]
# print(value)
# print(f'Czas: {value["date"]}, wartosc odczytu: {value["value"]}')

nazwaMiasta = "Wroclaw"
url = f'https://www.meteoprog.pl/pl/weather/{nazwaMiasta}/'
response = requests.get(url)

soup = BeautifulSoup(response.content)
dane = soup.find('ul', class_='today-hourly-weather hide-scroll').find_all('li')
table = []

for i in dane:
    temperature = i.find('span', class_='today-hourly-weather__temp').text.strip()
    pora_dnia = i.find('span', class_='today-hourly-weather__name').text.strip()
    print(temperature, pora_dnia)

# --------------------wykres liniowy-----------------
y = [1, 2, 3]
x = [6, 7, 8]
plt.plot(y, x)
# plt.show()
