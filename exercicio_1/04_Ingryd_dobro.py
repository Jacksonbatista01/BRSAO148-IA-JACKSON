'''
4 - Crie uma função em Python que receba um número como parâmetro e retorne o
o dobro desse número. Depois, chame essa função com um número fornecido pelo usuário
'''
# class cria um modelo para criar objetos que podem ser reutilizados
class Dobro:
    # solicita o numero ao usuario, o self é para usar os dados em outras funções
    def solicitacao(self):
        self.num = int(input("Coloque um numero: "))
    # Aqui é feito o calculo, lembrando que o self é para conectar os dados.
    def dobro(self):
        self.dobro_resultado = self.num * 2
        # O print da erro na def, então use o return
        return self.dobro_resultado
    # função de saida o self.solicitacao executa a função com o mesmo nome
    def saida(self):
        self.solicitacao()
        print(f"O dobro do seu número é {self.dobro()}")

# atribui o objeto
resultado = Dobro()
# Executa tudo
resultado.saida()