import requests

def consultar_cep(cep):
    cep = cep.replace("-", "").replace(".", "")
    
    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        response = requests.get(url)
        response.raise_for_status()  
        
        dados = response.json()

        if "erro" in dados:
            print(f"CEP {cep} não encontrado.")
        else:
            print(f"Informações do CEP {cep}:")
            print(f"Logradouro: {dados['logradouro']}")
            print(f"Bairro: {dados['bairro']}")
            print(f"Cidade: {dados['localidade']}")
            print(f"Estado: {dados['uf']}")
            print(f"CEP: {dados['cep']}")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao consultar o CEP: {e}")

cep_usuario = input("Digite o CEP que você deseja consultar (apenas números): ")

consultar_cep(cep_usuario)
