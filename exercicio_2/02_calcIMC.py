'''2- Calculadora de IMC.'''
'''Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa. 
O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário, 
calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.'''

# Função que calcula o IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)  # Fórmula do IMC

# Solicita o peso ao usuário
peso = float(input("Digite seu peso (em kg): "))

# Solicita a altura ao usuário
altura = float(input("Digite sua altura (em metros): "))

# Calcula o IMC
imc = calcular_imc(peso, altura)

# Classifica o IMC de acordo com a tabela padrão
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif 18.5 <= imc < 24.9:
    classificacao = "Peso normal"
elif 25 <= imc < 29.9:
    classificacao = "Sobrepeso"
elif 30 <= imc < 34.9:
    classificacao = "Obesidade grau 1"
elif 35 <= imc < 39.9:
    classificacao = "Obesidade grau 2"
else:
    classificacao = "Obesidade grau 3 (mórbida)"

# Exibe o IMC e a classificação
print(f"Seu IMC é: {imc:.2f}")
print(f"Classificação: {classificacao}")