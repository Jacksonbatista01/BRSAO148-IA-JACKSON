'''Crie um programa que permita a um professor registrar as notas de uma turma. O programa deve continuar solicitando notas até que o professor digite 'fim'. Notas válidas são de 0 a 10. O programa deve ignorar notas inválidas e continuar solicitando. No final, deve exibir a média da turma.'''

print("=== Registro de Notas da Turma ===")
print("Digite as notas dos alunos (de 0 a 10).")
print("Digite 'fim' para encerrar e calcular a média.\n")

notas = []

while True:
    entrada = input("Digite a nota: ")

    if entrada.lower() == 'fim':
        break  # Encerra a coleta de notas

    try:
        nota = float(entrada)  # Tenta converter a entrada para número real

        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("⚠️ Nota inválida. Digite um valor entre 0 e 10.")
    except ValueError:
        print("⚠️ Entrada inválida. Digite um número ou 'fim'.")

# Cálculo e exibição da média
if notas:
    media = sum(notas) / len(notas)
    print(f"\n✅ Média da turma: {media:.2f}")
else:
    print("\nNenhuma nota válida foi registrada.")