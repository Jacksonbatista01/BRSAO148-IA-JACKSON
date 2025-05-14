'''Crie um programa para registrar as temperaturas de vários dias. O usuário deve digitar a temperatura em graus Celsius (ex: 25.5). O programa continua coletando até que o usuário digite "fim" ou colete 7 temperaturas. Valores inválidos devem ser ignorados. Ao final, exiba a média das temperaturas registradas.'''

print("=== Registro de Temperaturas ===")
print("Digite até 7 temperaturas em °C (ex: 25.5).")
print("Digite 'fim' para encerrar antecipadamente.\n")

temperaturas = []

for i in range(7):
    entrada = input(f"Digite a {i + 1}ª temperatura: ")

    if entrada.lower() == "fim":
        break  # Encerra se o usuário digitar 'fim'

    try:
        temp = float(entrada)  # Tenta converter para número decimal
        temperaturas.append(temp)
    except ValueError:
        print("⚠️ Entrada inválida. Digite um número (ex: 22.0) ou 'fim'.")
        continue  # Ignora entrada inválida

# Exibe a média final
if temperaturas:
    media = sum(temperaturas) / len(temperaturas)
    print(f"\n🌡️ Temperaturas registradas: {temperaturas}")
    print(f"📊 Média das temperaturas: {media:.2f}°C")
else:
    print("\nNenhuma temperatura válida foi registrada.")