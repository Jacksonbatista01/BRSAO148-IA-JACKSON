'''Crie um programa que gera uma senha aleatória com o módulo random, utilizando caracteres especiais, possibilitando o usuário a informar a quantidade de caracteres dessa senha aleatória.'''

import random
import string

def gerar_senha(tamanho):
    # Conjunto de caracteres: letras + números + especiais
    caracteres = string.ascii_letters + string.digits + string.punctuation
    # Gera senha com o número de caracteres solicitado
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def main():
    print("=== Gerador de Senha Aleatória ===")
    try:
        tamanho = int(input("Informe a quantidade de caracteres para a senha: "))
        if tamanho <= 0:
            print("Por favor, insira um número maior que zero.")
            return
        senha = gerar_senha(tamanho)
        print(f"\nSenha gerada: {senha}")
    except ValueError:
        print("Entrada inválida! Por favor, insira um número inteiro.")

if __name__ == "__main__":
    main()