'''Crie um programa com uma função que cadastre alunos e suas respectivas notas.
O sistema deve:
Solicitar o nome do aluno.
Solicitar 3 notas válidas (entre 0 e 10).
Armazenar os dados em um dicionário, onde a chave é o nome e o valor é uma lista de notas.
Permitir o cadastro de vários alunos até que o usuário digite "fim".
Exibir ao final:
A lista de alunos e suas médias.
O aluno com a maior média.
Use def para as funcionalidades e try/except para tratar entradas inválidas.'''

# Função para cadastrar alunos e suas notas
def cadastrar_alunos():
    alunos = {}

    while True:
        nome = input("\nDigite o nome do aluno (ou 'fim' para encerrar): ").strip()
        if nome.lower() == "fim":
            break
        if nome == "":
            print("⚠️ Nome não pode ser vazio.")
            continue

        notas = []
        for i in range(1, 4):
            while True:
                try:
                    nota = float(input(f"Digite a {i}ª nota de {nome} (0 a 10): "))
                    if 0 <= nota <= 10:
                        notas.append(nota)
                        break
                    else:
                        print("⚠️ Nota fora do intervalo permitido (0 a 10).")
                except ValueError:
                    print("⚠️ Entrada inválida. Digite um número.")

        alunos[nome] = notas
        print(f"✅ Aluno {nome} cadastrado com sucesso.")

    return alunos

# Função para calcular e exibir as médias
def exibir_resultados(alunos):
    print("\n=== Médias dos Alunos ===")
    maior_media = -1
    aluno_top = ""

    for nome, notas in alunos.items():
        media = sum(notas) / len(notas)
        print(f"{nome}: Média = {media:.2f}")
        if media > maior_media:
            maior_media = media
            aluno_top = nome

    if aluno_top:
        print(f"\n🏆 Aluno com a maior média: {aluno_top} ({maior_media:.2f})")
    else:
        print("Nenhum aluno cadastrado.")

# Programa principal
print("=== Cadastro de Alunos e Notas ===")
alunos_cadastrados = cadastrar_alunos()
exibir_resultados(alunos_cadastrados)