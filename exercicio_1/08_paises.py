'''8 - Crie um programa que armazene nomes de países e suas capitais em um dicionário. O usuário digita o nome do país e o programa mostra a capital correspondente.'''

# Dicionário com países e suas capitais
paises_capitais = {
    "Argentina": "Buenos Aires",
    "Itália": "Roma",
    "Austrália": "Camberra",
    "Egito": "Cairo",
    "Índia": "Nova Délhi"
}

# Solicita o nome do país ao usuário
pais = input("Digite o nome de um país: ")

# Verifica se o país está no dicionário
if pais in paises_capitais:
    print("A capital de", pais, "é", paises_capitais[pais])
else:
    print("País não encontrado no sistema.")