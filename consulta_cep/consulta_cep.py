import requests

class ConsultaCEPError(Exception):
    pass

def formatar_cep(cep):
    return ''.join(filter(str.isdigit, cep))

def buscar_dados_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    
    if response.status_code != 200:
        raise ConsultaCEPError(f"Erro ao consultar o CEP: {response.status_code}")
    
    return response.json()

def extrair_dados_relevantes(dados):
    return {
        "cep": dados.get("cep"),
        "logradouro": dados.get("logradouro"),
        "complemento": dados.get("complemento"),
        "unidade": dados.get("unidade"),
        "bairro": dados.get("bairro"),
        "localidade": dados.get("localidade"),
        "uf": dados.get("uf"),
        "estado": dados.get("estado"),
        "regiao": dados.get("regiao"),
        "ibge": dados.get("ibge"),
        "gia": dados.get("gia"),
        "ddd": dados.get("ddd"),
        "siafi": dados.get("siafi")
    }

def consulta_cep(cep):
    cep_formatado = formatar_cep(cep)
    dados = buscar_dados_cep(cep_formatado)
    return extrair_dados_relevantes(dados)

def exibir_dados_cep(dados_cep):
    for chave, valor in dados_cep.items():
        print(f"{chave}: {valor}")

if __name__ == "__main__":
    cep_input = "01311200"  #substitua pelo CEP desejado    
    try:
        resultado = consulta_cep(cep_input)
        exibir_dados_cep(resultado)
    except ConsultaCEPError as e:
        print(f"Ocorreu um erro: {e}")