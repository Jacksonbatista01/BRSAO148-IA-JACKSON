'''Crie uma função que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de gorjeta desejada.
A função deve receber dois parâmetros:
valor_conta (float): O valor total da conta
porcentagem_gorjeta (float): A porcentagem da gorjeta (por exemplo, 10 para 10%)'''

# Função para calcular a gorjeta
def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta

# Exemplo de uso
print("=== Calculadora de Gorjeta ===")

try:
    valor = float(input("Digite o valor da conta (R$): "))
    porcentagem = float(input("Digite a porcentagem da gorjeta (%): "))

    gorjeta_calculada = calcular_gorjeta(valor, porcentagem)
    total = valor + gorjeta_calculada

    print(f"\n💰 Gorjeta: R$ {gorjeta_calculada:.2f}")
    print(f"🧾 Total com gorjeta: R$ {total:.2f}")

except ValueError:
    print("⚠️ Entrada inválida. Certifique-se de digitar números válidos.")