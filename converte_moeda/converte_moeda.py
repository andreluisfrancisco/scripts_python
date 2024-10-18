import requests

def conversor_moeda(valor, de, para):
    url = f'https://api.exchangerate-api.com/v4/latest/{de}'
    response = requests.get(url).json()
    taxa = response['rates'][para]
    return valor * taxa

print(conversor_moeda(1, 'USD', 'BRL'))
