import requests

def verificar_site(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return f'{url} está online'
        else:
            return f'{url} está offline'
    except requests.ConnectionError:
        return f'{url} não está acessível'

print(verificar_site('https://www.python.org'))
