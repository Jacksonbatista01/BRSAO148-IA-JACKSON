'''Peça ao usuário para digitar palavras. Armazene apenas as palavras com mais de 5 letras em uma lista. Se a palavra for "parar", o programa encerra (break). Se a palavra for numérica (como "123"), ignore com continue. Use try/except para garantir que só palavras (strings) sejam processadas. No final, exiba a lista das palavras longas inseridas.'''

print("=== Coletor de Palavras Longas ===")
print("Digite palavras com mais de 5 letras.")
print("Digite 'parar' para encerrar.\n")

palavras_longas = []

while True:
    try:
        palavra = input("Digite uma palavra: ").strip()

        if palavra.lower() == "parar":
            break  # Encerra o programa

        if palavra.isnumeric():
            print("⚠️ Palavra numérica ignorada.")
            continue  # Ignora entradas numéricas

        if not isinstance(palavra, str):
            raise ValueError("Entrada inválida.")

        if len(palavra) > 5:
            palavras_longas.append(palavra)
        else:
            print("⚠️ Palavra com 5 ou menos letras ignorada.")

    except Exception as e:
        print(f"⚠️ Erro ao processar a entrada: {e}")
        continue

# Exibe as palavras válidas inseridas
print("\n📚 Palavras com mais de 5 letras:")
if palavras_longas:
    for i, p in enumerate(palavras_longas, 1):
        print(f"{i}. {p}")
else:
    print("Nenhuma palavra longa foi inserida.")