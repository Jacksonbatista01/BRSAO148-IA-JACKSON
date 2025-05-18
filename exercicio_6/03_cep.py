'''Desenvolva um programa que consulte informações de endereço a partir de um CEP fornecido pelo usuário, utilizando a API ViaCEP. O programa deve exibir o logradouro, bairro, cidade e estado correspondentes ao CEP consultado.
** Instale o modulo requests - pip install requests **
URL da API ViaCEP, passando o CEP informado
    url = f"https://viacep.com.br/ws/{cep}/json/"'''

import requests

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        resposta = requests.get(url)
        resposta.raise_for_status()  # Verifica se houve erro na requisição

        dados = resposta.json()

        if "erro" in dados:
            print("❌ CEP não encontrado.")
        else:
            print("\n📍 Informações do endereço:")
            print(f"Logradouro: {dados.get('logradouro', 'N/A')}")
            print(f"Bairro:     {dados.get('bairro', 'N/A')}")
            print(f"Cidade:     {dados.get('localidade', 'N/A')}")
            print(f"Estado:     {dados.get('uf', 'N/A')}")

    except requests.exceptions.RequestException as erro:
        print("Erro na requisição:", erro)

def main():
    cep = input("Digite o CEP (somente números): ").strip()

    if len(cep) == 8 and cep.isdigit():
        consultar_cep(cep)
    else:
        print("⚠️ CEP inválido. Digite exatamente 8 números.")

if __name__ == "__main__":
    main()