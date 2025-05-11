'''7- Verificador de Palíndromo'''
'''Crie um programa que solicite uma palavra e verifique se ela é um palíndromo (ou seja, se pode ser lida da mesma forma de trás para frente).'''

# Solicita a palavra ao usuário
palavra = input("Digite uma palavra: ")

# Remove espaços e converte para minúsculas para garantir a comparação correta
palavra_formatada = palavra.replace(" ", "").lower()

# Verifica se a palavra é igual à sua versão invertida
if palavra_formatada == palavra_formatada[::-1]:
    print(f"A palavra '{palavra}' é um palíndromo.")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")