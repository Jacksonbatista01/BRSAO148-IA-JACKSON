'''Crie um programa que gera um perfil de usuário aleatório usando a API 'Random User Generator'. O programa deve exibir o nome, email e país do usuário gerado.
** Instale o modulo requests - pip install requests **
URL da API que retorna um usuário aleatório no formato JSON
    url = "https://randomuser.me/api/"'''

import requests

def gerar_usuario():
    url = "https://randomuser.me/api/"
    
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()  # Verifica se houve erro na resposta

        dados = resposta.json()
        usuario = dados['results'][0]

        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']

        print("=== Perfil de Usuário Gerado ===")
        print(f"Nome:  {nome}")
        print(f"E-mail: {email}")
        print(f"País:  {pais}")

    except requests.exceptions.RequestException as erro:
        print("Erro ao acessar a API:", erro)
    except KeyError:
        print("Erro ao processar os dados da resposta.")

if __name__ == "__main__":
    gerar_usuario()