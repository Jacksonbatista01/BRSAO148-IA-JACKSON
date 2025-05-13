'''Crie um programa onde o computador escolhe um número entre 1 e 10, e o usuário deve adivinhar qual é. O programa continua pedindo tentativas até que o usuário acerte. Use while, break e True para controlar o fluxo.'''

import random

# O computador escolhe um número entre 1 e 10
numero_secreto = random.randint(1, 10)

print("Tente adivinhar o número que estou pensando (entre 1 e 10)!")

# Loop infinito até o usuário acertar
while True:
    tentativa = int(input("Digite sua tentativa: "))

    if tentativa == numero_secreto:
        print("🎉 Parabéns! Você acertou o número!")
        break
    else:
        print("❌ Errou! Tente novamente.")