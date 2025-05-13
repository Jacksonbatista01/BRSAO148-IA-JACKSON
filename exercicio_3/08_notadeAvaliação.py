'''Crie um programa que solicita a nota de avaliação de um restaurante (de 0 a 5) e exibe a quantidade de estrelas equivalente, juntamente com uma mensagem personalizada. Use if, elif e else para lidar com diferentes faixas de nota.'''

# Solicita a nota do restaurante
nota = float(input("Avalie o restaurante (de 0 a 5): "))

# Verifica a faixa da nota e imprime estrelas com mensagem personalizada
if nota < 0 or nota > 5:
    print("Nota inválida. Por favor, digite um valor entre 0 e 5.")
elif nota == 0:
    print("★☆☆☆☆ - Péssima experiência. 😞")
elif nota <= 2:
    print("★★☆☆☆ - Poderia melhorar bastante. 😕")
elif nota <= 3.5:
    print("★★★☆☆ - Experiência razoável. 👍")
elif nota <= 4.5:
    print("★★★★☆ - Ótimo atendimento e comida! 😋")
else:
    print("★★★★★ - Excelente! Voltarei com certeza! 🌟")
