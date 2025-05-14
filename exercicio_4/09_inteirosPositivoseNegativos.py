'''Solicite ao usuário números inteiros até que ele digite "0". Armazene os positivos e negativos separadamente em duas listas. Ignore valores não inteiros com try/except. No final, mostre quantos positivos e negativos foram inseridos.'''

print("=== Classificador de Números ===")
print("Digite números inteiros. Digite '0' para encerrar.\n")

positivos = []
negativos = []

while True:
    entrada = input("Digite um número: ")

    if entrada == "0":
        break  # Encerra o programa

    try:
        numero = int(entrada)

        if numero > 0:
            positivos.append(numero)
        elif numero < 0:
            negativos.append(numero)

    except ValueError:
        print("⚠️ Entrada inválida. Digite apenas números inteiros.")
        continue  # Ignora e pede outro número

# Exibe os resultados
print("\n📊 Resultado:")
print(f"Números positivos inseridos: {len(positivos)} ➜ {positivos}")
print(f"Números negativos inseridos: {len(negativos)} ➜ {negativos}")