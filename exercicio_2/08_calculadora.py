'''8- Calculadora Simples'''
'''Crie um programa que simule uma calculadora simples. O usuário deve informar dois números e a operação desejada (+, -, *, /) e o programa deve exibir o resultado da operação'''

# Solicita os dois números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Solicita a operação desejada
operacao = input("Digite a operação (+, -, *, /): ")

# Verifica qual operação será realizada e executa
if operacao == "+":
    resultado = num1 + num2
    print(f"Resultado: {num1} + {num2} = {resultado}")
elif operacao == "-":
    resultado = num1 - num2
    print(f"Resultado: {num1} - {num2} = {resultado}")
elif operacao == "*":
    resultado = num1 * num2
    print(f"Resultado: {num1} * {num2} = {resultado}")
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
        print(f"Resultado: {num1} / {num2} = {resultado}")
    else:
        print("Erro: divisão por zero não é permitida.")
else:
    print("Operação inválida. Use apenas +, -, * ou /.")