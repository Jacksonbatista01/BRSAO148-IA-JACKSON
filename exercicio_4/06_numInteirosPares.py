'''Peça ao usuário que digite 10 números inteiros. Armazene apenas os números pares válidos em uma lista. Use try/except para capturar erros, continue para ignorar números ímpares ou inválidos, e exiba a lista final ao terminar.'''

print("=== Coletor de Números Pares ===")
print("Digite 10 números inteiros. Apenas os pares serão armazenados.\n")

numeros_pares = []
tentativas = 0

while tentativas < 10:
    entrada = input(f"Digite o {tentativas + 1}º número: ")

    try:
        numero = int(entrada)

        if numero % 2 == 0:
            numeros_pares.append(numero)
        else:
            print("⚠️ Número ímpar ignorado.")
        
        tentativas += 1  # Conta a tentativa mesmo se o número for ímpar

    except ValueError:
        print("⚠️ Entrada inválida. Digite apenas números inteiros.")
        continue  # Não conta a tentativa se a entrada for inválida

# Exibe o resultado
print("\n✅ Números pares armazenados:")
print(numeros_pares if numeros_pares else "Nenhum número par foi inserido.")