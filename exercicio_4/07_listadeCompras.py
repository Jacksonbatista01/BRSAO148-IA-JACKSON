'''Crie um programa que permita que o usuário monte uma lista de compras digitando nomes de produtos. O usuário pode digitar até 10 itens. Se digitar "fim", o programa para imediatamente (break). Se o item for vazio (só apertar Enter), ele é ignorado com continue. Use try/except para garantir que apenas strings sejam inseridas.'''

print("=== Lista de Compras ===")
print("Digite até 10 itens. Digite 'fim' para encerrar.\n")

lista_compras = []

for i in range(10):
    try:
        item = input(f"Digite o {i + 1}º item: ").strip()

        if item.lower() == 'fim':
            break  # Encerra o loop se o usuário digitar "fim"

        if item == "":
            print("⚠️ Item vazio ignorado.")
            continue  # Ignora entradas vazias

        # Verificação explícita para garantir que seja uma string
        if not isinstance(item, str):
            raise ValueError("Entrada inválida. Insira um texto.")

        lista_compras.append(item)

    except Exception as e:
        print(f"⚠️ Erro: {e}")
        continue

# Exibe a lista final de compras
print("\n🛒 Sua lista de compras:")
if lista_compras:
    for i, produto in enumerate(lista_compras, 1):
        print(f"{i}. {produto}")
else:
    print("Nenhum item foi adicionado.")