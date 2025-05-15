'''Crie uma função que receba uma lista de notas (valores float) e calcule a média. O programa principal deverá solicitar ao usuário o nome de um aluno e suas 3 notas, e então utilizar a função para calcular e exibir a média com duas casas decimais.'''

# Função que calcula a média de uma lista de notas
def calcular_media(notas):
    return sum(notas) / len(notas)

# Programa principal
print("=== Cálculo de Média do Aluno ===")

# Solicita o nome do aluno
nome_aluno = input("Digite o nome do aluno: ")

notas = []

# Solicita 3 notas válidas
for i in range(1, 4):
    while True:
        try:
            nota = float(input(f"Digite a {i}ª nota (0 a 10): "))
            if 0 <= nota <= 10:
                notas.append(nota)
                break
            else:
                print("⚠️ A nota deve estar entre 0 e 10.")
        except ValueError:
            print("⚠️ Entrada inválida. Digite um número decimal.")

# Calcula e exibe a média
media = calcular_media(notas)
print(f"\n📚 Aluno: {nome_aluno}")
print(f"📝 Notas: {notas}")
print(f"📊 Média: {media:.2f}")