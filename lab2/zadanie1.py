import requests

url = 'https://api.gios.gov.pl/pjp-api/rest/station/findAll'

def check_url(url: str) -> bool:
    response = requests.get(url)
    if(200<= response.status_code <300 ):
        return True
    else:
        return False

print(check_url(url))
