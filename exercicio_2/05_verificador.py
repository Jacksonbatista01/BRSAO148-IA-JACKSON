'''5- Verificador de Número Primo'''
'''Crie um programa que solicite um número inteiro positivo ao usuário e verifique se ele é um número primo. Um número primo só é divisível por 1 e por ele mesmo.'''

# Solicita um número inteiro positivo ao usuário
numero = int(input("Digite um número inteiro positivo: "))

# Verifica se o número é válido
if numero <= 1:
    print("O número deve ser maior que 1.")
else:
    # Assume que o número é primo até provar o contrário
    eh_primo = True

    # Verifica se existe algum divisor além de 1 e ele mesmo
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            eh_primo = False
            break  # Se encontrou divisor, não é primo

    # Mostra o resultado
    if eh_primo:
        print(f"O número {numero} é primo.")
    else:
        print(f"O número {numero} não é primo.")