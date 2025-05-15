'''Crie uma função que calcule a idade de uma pessoa em dias, com base no ano de nascimento informado pelo usuário.
O programa deve considerar o ano atual como base para o cálculo.
Use try/except para tratar erros de entrada e valide que o ano não pode ser maior que o ano atual.'''

from datetime import date

# Função para calcular a idade em dias
def calcular_idade_em_dias(ano_nascimento):
    ano_atual = date.today().year
    if ano_nascimento > ano_atual:
        raise ValueError("O ano de nascimento não pode ser no futuro.")
    idade_anos = ano_atual - ano_nascimento
    idade_dias = idade_anos * 365  # Aproximação, sem contar anos bissextos
    return idade_dias

# Programa principal
print("=== Cálculo de Idade em Dias ===")

try:
    entrada = input("Digite seu ano de nascimento (ex: 1990): ")
    ano = int(entrada)

    idade_dias = calcular_idade_em_dias(ano)
    print(f"📅 Sua idade aproximada é de {idade_dias} dias.")

except ValueError as ve:
    print(f"⚠️ Erro: {ve}")
except Exception:
    print("⚠️ Entrada inválida. Por favor, digite um ano válido.")