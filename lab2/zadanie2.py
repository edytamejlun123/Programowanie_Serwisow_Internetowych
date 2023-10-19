import requests
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup

nazwaMiasta = "Wroclaw"
url = f'https://www.meteoprog.pl/pl/weather/{nazwaMiasta}/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
dane = soup.find('ul', class_='today-hourly-weather hide-scroll').find_all('li')
x_temperature = []
y_poraDnia = []
for i in dane:
    temperature = i.find('span', class_='today-hourly-weather__temp').text.strip()
    pora_dnia = i.find('span', class_='today-hourly-weather__name').text.strip()
    y_poraDnia.append(pora_dnia)
    temp = temperature.replace("+", "").replace("°", "").strip()
    temperature_int = int(temp)
    x_temperature.append(temperature_int)
    print(temperature_int, pora_dnia)

plt.plot(y_poraDnia, x_temperature)
plt.show()
