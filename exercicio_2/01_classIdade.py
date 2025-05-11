'''1- Classificador de Idade.'''
'''Crie um programa que solicite a idade do usuário e classifique-o 
em uma das seguintes categorias.'''

# Solicita a idade ao usuário
idade = int(input("Digite sua idade: "))

# Classifica a idade em faixas etárias
if idade < 0:
    print("Idade inválida.")
elif idade < 12:
    print("Você é uma criança.")
elif idade < 18:
    print("Você é um adolescente.")
elif idade < 60:
    print("Você é um adulto.")
else:
    print("Você é um idoso.")