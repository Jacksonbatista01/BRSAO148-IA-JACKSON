'''Crie um programa que solicite ao usuário uma nota (de 0 a 10) e exiba uma mensagem dizendo se o aluno foi reprovado, em recuperação ou aprovado.
Use as estruturas de decisão if, elif e else.'''

# Solicita a nota do usuário
nota = float(input("Digite a nota do aluno (de 0 a 10): "))

# Verifica e exibe o resultado com base na nota
if nota < 0 or nota > 10:
    print("Nota inválida. Por favor, digite um valor entre 0 e 10.")
elif nota < 5:
    print("Aluno reprovado.")
elif nota < 7:
    print("Aluno em recuperação.")
else:
    print("Aluno aprovado.")