'''Crie um programa que percorre uma lista de números inteiros e imprime apenas os que são números primos. Use o for para iterar, if para a verificação e continue para pular os que não são primos'''

# Lista de números inteiros
numeros = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 17, 19, 20]

print("Números primos encontrados:")

# Percorre a lista
for numero in numeros:
    if numero < 2:
        continue  # Números menores que 2 não são primos

    # Verifica se o número é primo
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            # Se for divisível, não é primo — pula para o próximo
            continue_outer = True
            break
    else:
        # Se não encontrou nenhum divisor, é primo
        print(numero)
        continue

    continue  # Usado para pular o print se não for primo