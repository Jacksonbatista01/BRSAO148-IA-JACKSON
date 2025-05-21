import csv
import statistics

def processar_logs(caminho_arquivo):
    tempos = []

    try:
        with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                tempo = float(linha['tempo_execucao'])
                tempos.append(tempo)

        media = statistics.mean(tempos)
        desvio_padrao = statistics.stdev(tempos)

        print(f"Média de tempo de execução: {media:.2f} segundos")
        print(f"Desvio padrão: {desvio_padrao:.2f} segundos")

    except FileNotFoundError:
        print("Arquivo não encontrado. Verifique o caminho e o nome do arquivo.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    processar_logs("logs_treinamento.csv")