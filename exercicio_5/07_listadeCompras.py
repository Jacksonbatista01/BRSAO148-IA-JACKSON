'''Crie um programa que permita ao usuário montar uma lista de compras. O usuário poderá adicionar itens até digitar "fim". Ao final, o programa exibirá todos os itens da lista. O programa deve estar estruturado com uma função main() e ser executado com if __name__ == "__main__":.'''

def main():
    print("🛒 Lita de compras")
    print("Digite os itens desejados. Para encerrar, digite 'fim'.\n")

    lista_compras = []

    while True:
        item = input("Adicione um item: ").strip()
        if item.lower() == "fim":
            break
        if item == "":
            print("⚠️ Item vazio ignorado.")
            continue
        lista_compras.append(item)
        print(f"✅ '{item}' adicionado à lista.")

    print("\n📋 Parabéns, voce criou uma lista de compras das mais caras kkkkk:")
    if lista_compras:
        for i, produto in enumerate(lista_compras, 1):
            print(f"{i}. {produto}")
    else:
        print("Nenhum item foi adicionado.")

# Execução principal
if __name__ == "__main__":
    main()