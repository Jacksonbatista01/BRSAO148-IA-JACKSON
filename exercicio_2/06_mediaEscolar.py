'''6- Calculadora de Média Escolar'''
'''Desenvolva um programa que solicite o nome de um aluno e suas 3 notas. O programa deve calcular a média e informar se o aluno foi aprovado (média >= 7), está em recuperação (5 <= média < 7) ou foi reprovado (média < 5).'''

# Solicita o nome do aluno
nome = input("Digite o nome do aluno: ")

# Solicita as três notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcula a média das notas
media = (nota1 + nota2 + nota3) / 3

# Exibe a média com duas casas decimais
print(f"\nMédia de {nome}: {media:.2f}")

# Verifica a situação do aluno
if media >= 7:
    print("Situação: Aprovado ✅")
elif media >= 5:
    print("Situação: Recuperação ⚠️")
else:
    print("Situação: Reprovado ❌")