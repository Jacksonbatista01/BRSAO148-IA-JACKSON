'''Crie um programa que faça uma contagem regressiva a partir de um número informado pelo usuário até 0. O programa deve mostrar cada número da contagem e, ao final, exibir "FIM!".'''

# Solicita o número inicial para a contagem regressiva
numero = int(input("Digite o número para iniciar a contagem regressiva: "))

# Contagem regressiva com decremento de 2 usando while
while numero >= 0:
    print(numero)
    numero -= 2  # Decrementa 2 a cada iteração

# Exibe "FIM!" ao final
print("FIM!")
