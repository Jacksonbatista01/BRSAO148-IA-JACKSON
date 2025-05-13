'''Crie um programa que solicite um número ao usuário e exiba a tabuada desse número de 1 a 10, utilizando a estrutura de repetição for.'''

# Solicita o número para o usuário
numero = int(input("Digite um número para ver a tabuada: "))

# Exibe a tabuada de 1 a 10
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

