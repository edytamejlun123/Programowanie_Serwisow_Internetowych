import requests as rs

url = 'http://wmii.uwm.edu.pl/'

response = rs.get(url)

print(response)

#200-299 url prawidłowy
print('kod odpowiedzi: ', response.status_code)
print(response.headers)
print('tresc odpowiedzi: ', response.content.decode('utf-8'))

