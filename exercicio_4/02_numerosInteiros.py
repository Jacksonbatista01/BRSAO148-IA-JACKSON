'''Crie um programa que solicite ao usuário que insira números inteiros. O programa deve continuar solicitando números até que o usuário digite 'fim'. Para cada número inserido, o programa deve informar se é par ou ímpar. Se o usuário inserir algo que não seja um número inteiro, o programa deve informar o erro e continuar. No final, o programa deve exibir a quantidade de números pares e ímpares inseridos.'''

# Inicializa os contadores
pares = 0
impares = 0

print("Digite números inteiros para saber se são pares ou ímpares.")
print("Digite 'fim' para encerrar o programa.\n")

# Loop principal
while True:
    entrada = input("Digite um número (ou 'fim' para sair): ")

    if entrada.lower() == 'fim':
        break  # Encerra o loop se o usuário digitar 'fim'

    try:
        numero = int(entrada)  # Tenta converter a entrada para inteiro

        if numero % 2 == 0:
            print("✅ É um número **par**.\n")
            pares += 1
        else:
            print("✅ É um número **ímpar**.\n")
            impares += 1

    except ValueError:
        # Trata o caso em que o usuário digita algo que não é um número inteiro
        print("⚠️ Entrada inválida. Por favor, digite apenas números inteiros.\n")

# Exibe o resumo final
print("=== FIM DO PROGRAMA ===")
print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")