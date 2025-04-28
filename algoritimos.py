# algoritmo de busca - linear
'''def busca (lista, nome_procurado):
    for i in range(len(lista)):
        if lista[i] == nome_procurado:
            return i + 1 # retorna para a posição
    return -1 # não encontrou
nomes = ["Maria", "Ana", "João", "Pedro"]
posicao = busca(nomes, "Ana")
nome_procurado = input('Qual nome você quer procurar? ')
print("Ana está na posição:", posicao)'''

# algoritmo de busca - binária
def binaria (lista, valor_procurado):
    inicio = 0
    fim = len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == valor_procurado:
            return meio
        elif lista[meio] < valor_procurado:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1
numeros = [1, 3, 5, 7, 9, 11, 13, 15]
posicao = binaria(numeros, 15)
print("Número encontrado na posição:", posicao)