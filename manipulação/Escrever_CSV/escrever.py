'''Crie um script em Python que escreva dados em um arquivo CSV. O arquivo CSV deve conter informações de pessoas, com colunas Nome, Idade e Cidade.
escrever_csv.py'''

# Importa o módulo csv que permite manipular arquivos CSV
import csv

# Define uma função para solicitar dados ao usuário e salvar em CSV
def escrever_dados_csv(nome_arquivo):
    """
    Solicita ao usuário que insira dados de pessoas e grava no arquivo CSV.
    
    Parâmetro:
    - nome_arquivo (str): nome do arquivo CSV que será criado.
    """
    # Abre o arquivo no modo escrita (write), e cria se não existir
    try:
        with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo:
            # Cria um escritor CSV para escrever os dados
            escritor = csv.writer(arquivo)

            # Escreve o cabeçalho do arquivo CSV
            escritor.writerow(['Nome', 'Idade', 'Cidade'])

            print("Digite os dados das pessoas. Para encerrar, digite 'fim' no nome.\n")

            # Loop para inserir várias pessoas
            while True:
                # Solicita o nome da pessoa
                nome = input("Nome: ").strip()
                
                # Se o usuário digitar 'fim', o loop é interrompido
                if nome.lower() == 'fim':
                    break

                # Solicita a idade e trata erro se não for número inteiro
                try:
                    idade = int(input("Idade: "))
                except ValueError:
                    print("Idade inválida. Digite um número inteiro.\n")
                    continue  # Volta para o início do laço

                # Solicita a cidade da pessoa
                cidade = input("Cidade: ").strip()

                # Escreve a linha no arquivo CSV com os dados coletados
                escritor.writerow([nome, idade, cidade])
                print("Pessoa adicionada com sucesso!\n")

        # Mensagem final após escrita do arquivo
        print(f"\nArquivo '{nome_arquivo}' criado com sucesso!")

    # Se ocorrer algum erro ao abrir ou escrever no arquivo, será tratado aqui
    except Exception as e:
        print(f"Erro ao escrever no arquivo: {e}")

# Ponto principal do programa
if __name__ == "__main__":
    """
    Este bloco é executado somente quando o script é rodado diretamente.
    Aqui chamamos a função para escrever os dados no CSV.
    """

    # Nome do arquivo CSV que será gerado
    nome_arquivo_csv = 'pessoas.csv'

    # Chama a função que coleta e grava os dados no arquivo CSV
    escrever_dados_csv(nome_arquivo_csv)