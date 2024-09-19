import requests

def buscarCep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'

    try:
        resposta = requests.get(url)
        resposta.raise_for_status()        
        dados_recebidos = resposta.json()
        return dados_recebidos
    except requests.exceptions.RequestException as e:
        return {"erro": str(e)}

def formatar_dados(dados):
    
    return (f"CEP: {dados.get('cep')}\n"
            f"Endereço: {dados.get('logradouro')}\n"
            f"Bairro: {dados.get('bairro')}\n"
            f"Cidade: {dados.get('localidade')}\n"
            f"Estado: {dados.get('uf')}")

def main():
    while True:
        cep = input("Digite o CEP (somente números, ou 'sair' para encerrar): ").strip()
        
        if cep.lower() == 'sair':
            print("Saindo do programa.")
            break

        dados = buscarCep(cep)

        if "erro" in dados:
            print("CEP inválido. Certifique-se de que o CEP possui 8 dígitos e contém apenas números.")
            continue

        print(formatar_dados(dados))

if __name__ == "__main__":
    main()
