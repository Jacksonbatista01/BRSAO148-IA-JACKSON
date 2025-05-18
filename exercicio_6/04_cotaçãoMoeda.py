'''Crie um programa que consulte a cotação atual de uma moeda estrangeira em relação ao Real Brasileiro (BRL). O usuário deve informar o código da moeda desejada (ex: USD, EUR, GBP), e o programa deve exibir o valor atual, máximo e mínimo da cotação, além da data e hora da última atualização. Utilize a API da AwesomeAPI para obter os dados de cotação.
** Instale o modulo requests - pip install requests **
URL da API com base na moeda informada
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"'''

import requests

def consultar_cotacao(moeda):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

    try:
        resposta = requests.get(url)
        resposta.raise_for_status()  # Lança exceção se erro na resposta

        dados = resposta.json()
        chave = f"{moeda}BRL"

        if chave in dados:
            cotacao = dados[chave]
            print(f"\n💱 Cotação {moeda} para BRL:")
            print(f"Valor Atual: R$ {cotacao['bid']}")
            print(f"Valor Mínimo: R$ {cotacao['low']}")
            print(f"Valor Máximo: R$ {cotacao['high']}")
            print(f"Data: {cotacao['create_date']}")
        else:
            print("❌ Moeda não encontrada ou código incorreto.")

    except requests.exceptions.RequestException as erro:
        print("Erro na requisição:", erro)

def main():
    print("=== Consulta de Cotação ===")
    moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ").strip().upper()

    if moeda.isalpha() and len(moeda) == 3:
        consultar_cotacao(moeda)
    else:
        print("⚠️ Código inválido. Use apenas 3 letras (ex: USD, EUR).")

if __name__ == "__main__":
    main()