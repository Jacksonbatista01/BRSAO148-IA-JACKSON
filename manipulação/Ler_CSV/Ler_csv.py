import pandas as pd  # Importa a biblioteca Pandas para manipulação de dados

# Nome do arquivo CSV a ser lido
arquivo_csv = "dados_pessoas.csv"

try:
    # Tenta ler o arquivo CSV e armazená-lo em um DataFrame do Pandas
    df = pd.read_csv(arquivo_csv)

    # Exibe uma mensagem antes de imprimir os dados
    print("\nDados do arquivo CSV:\n")

    # Exibe o DataFrame na tela
    print(df)

# Captura erro caso o arquivo não seja encontrado
except FileNotFoundError:
    print(f"Erro: O arquivo '{arquivo_csv}' não foi encontrado.")

# Captura erro caso o arquivo CSV esteja vazio
except pd.errors.EmptyDataError:
    print("Erro: O arquivo CSV está vazio.")

# Captura erro caso o arquivo tenha problemas de formatação (ex: delimitadores errados)
except pd.errors.ParserError:
    print("Erro: O arquivo CSV está com um formato inválido.")

# Captura qualquer outro erro inesperado
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")