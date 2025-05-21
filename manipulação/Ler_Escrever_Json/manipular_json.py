import json  # Importa a biblioteca JSON para manipulação de arquivos JSON

# Nome do arquivo JSON onde os dados serão gravados
arquivo_json = "dados_pessoa.json"

# Dados da pessoa que serão gravados no arquivo
dados = {
    "nome": "João",
    "idade": 25,
    "cidade": "São Paulo"
}

# Escrevendo os dados no arquivo JSON
with open(arquivo_json, "w", encoding="utf-8") as f:
    # Usa json.dump para converter os dados em formato JSON e gravá-los no arquivo
    json.dump(dados, f, indent=4)  # 'indent=4' formata o JSON com indentação para melhor leitura

# Exibe mensagem de sucesso ao gravar os dados no arquivo
print(f"Dados gravados em '{arquivo_json}' com sucesso!\n")

# Lendo os dados do arquivo JSON
try:
    # Abre o arquivo JSON para leitura
    with open(arquivo_json, "r", encoding="utf-8") as f:
        # Usa json.load para carregar os dados do arquivo JSON para um dicionário Python
        dados_lidos = json.load(f)
    
    # Exibe os dados lidos do arquivo JSON, formatados de forma legível
    print("Dados lidos do arquivo JSON:")
    print(json.dumps(dados_lidos, indent=4, ensure_ascii=False))  # 'ensure_ascii=False' para manter caracteres especiais

except FileNotFoundError:
    # Captura erro caso o arquivo JSON não seja encontrado
    print(f"Erro: O arquivo '{arquivo_json}' não foi encontrado.")
except json.JSONDecodeError:
    # Captura erro caso o arquivo JSON tenha formato inválido
    print("Erro: O arquivo JSON está com um formato inválido.")
except Exception as e:
    # Captura qualquer outro erro inesperado
    print(f"Ocorreu um erro inesperado: {e}")