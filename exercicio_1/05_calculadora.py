'''5 - Crie um programa em Python que peça dois números e uma operação matemática (+, -, * ou /), e mostre o resultado de acordo com a operação escolhida.'''

# Função que realiza a operação escolhida
def calcular(numero1, numero2, operacao):
    if operacao == '+':
        return numero1 + numero2
    elif operacao == '-':
        return numero1 - numero2
    elif operacao == '*':
        return numero1 * numero2
    elif operacao == '/':
        # Verifica se o segundo número é zero antes de dividir
        if numero2 != 0:
            return numero1 / numero2
        else:
            return "Erro: divisão por zero!"
    else:
        return "Operação inválida!"

# Solicita ao usuário o primeiro número
num1 = float(input("Digite o primeiro número: "))

# Solicita ao usuário o segundo número
num2 = float(input("Digite o segundo número: "))

# Solicita ao usuário a operação desejada
op = input("Digite a operação (+, -, * ou /): ")

# Chama a função calcular e exibe o resultado
resultado = calcular(num1, num2, op)
print("Resultado:", resultado)