'''3- Conversor de Temperatura'''
'''Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.'''

# Função que realiza a conversão de temperatura
def converter_temperatura(valor, origem, destino):
    if origem == destino:
        return valor  # Nenhuma conversão necessária

    # Converter origem para Celsius primeiro
    if origem == "F":
        valor = (valor - 32) * 5/9
    elif origem == "K":
        valor = valor - 273.15

    # Agora converte de Celsius para destino
    if destino == "F":
        return (valor * 9/5) + 32
    elif destino == "K":
        return valor + 273.15
    elif destino == "C":
        return valor

# Solicita os dados do usuário
temperatura = float(input("Digite a temperatura: "))
origem = input("Digite a unidade de origem (C, F, K): ").upper()
destino = input("Digite a unidade de destino (C, F, K): ").upper()

# Verifica se as unidades são válidas
unidades_validas = {"C", "F", "K"}
if origem in unidades_validas and destino in unidades_validas:
    resultado = converter_temperatura(temperatura, origem, destino)
    print(f"{temperatura}°{origem} equivale a {resultado:.2f}°{destino}")
else:
    print("Unidade inválida. Use apenas C, F ou K.")