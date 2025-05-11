'''6 - Crie um programa que receba um número do usuário e diga se ele é positivo, negativo ou igual a zero.'''

# Solicita ao usuário que digite um número
numero = float(input("Digite um número: "))

# Verifica se o número é positivo, negativo ou zero
if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é igual a zero.")