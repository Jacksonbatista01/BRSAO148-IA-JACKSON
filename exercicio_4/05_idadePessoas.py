'''Crie um programa que solicite ao usuário a idade de várias pessoas. Armazene apenas idades válidas (entre 0 e 120) em uma lista. Use for, try/except, continue para ignorar entradas inválidas, e break para encerrar o programa se o usuário digitar "fim". No final, exiba a lista das idades válidas.'''

print("=== Registro de Idades ===")
print("Digite a idade das pessoas (entre 0 e 120).")
print("Digite 'fim' para encerrar.\n")

idades = []

# Usando for com um range grande para simular repetições indefinidas
for _ in range(1000):  # Valor alto para permitir muitas entradas
    entrada = input("Digite a idade: ")

    if entrada.lower() == 'fim':
        break  # Encerra o loop

    try:
        idade = int(entrada)

        if 0 <= idade <= 120:
            idades.append(idade)
        else:
            print("⚠️ Idade fora do intervalo permitido (0 a 120).")
            continue  # Volta para pedir outra entrada

    except ValueError:
        print("⚠️ Entrada inválida. Digite um número inteiro ou 'fim'.")
        continue  # Ignora entrada inválida

# Exibe as idades válidas coletadas
print("\n✅ Idades válidas registradas:")
print(idades if idades else "Nenhuma idade válida foi inserida.")