'''10 - Crie uma função que receba um número como argumento e retorne o quadrado desse número. Depois, chame essa função passando um número digitado pelo usuário.'''

# Função que calcula o quadrado de um número
def calcular_quadrado(numero):
    return numero ** 2  # Eleva o número ao quadrado

# Solicita ao usuário que digite um número
entrada = float(input("Digite um número para ver o quadrado: "))

# Chama a função e armazena o resultado
resultado = calcular_quadrado(entrada)

# Exibe o resultado
print("O quadrado de", entrada, "é", resultado)