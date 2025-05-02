'''
2 - Crie um programa
em Python que solicite um número do usuário e informe se ele é par ou ímpar.
'''

class Descubra:
    def solicitacao(self):
        self.num = float(input("Me diga um numero: "))
    
    def eh_par(self):
        if self.num % 2 == 0:
            return f"Seu numero {self.num} é par"
        else:
            return f"Seu numero {self.num} é impar"


resultado = Descubra()
resultado.solicitacao()
print(resultado.eh_par())