# Função que retorna o dobro de um número
def dobro(numero):
    return numero * 2

# Solicitar um número ao usuário
num = int(input("Digite um número: "))

# Chamar a função e exibir o resultado
resultado = dobro(num)
print(f"O dobro de {num} é {resultado}")