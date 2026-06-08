import csv  # Importa a biblioteca para leitura de arquivos CSV

def ler_csv(caminho):
    """
    Função responsável por ler um arquivo CSV contendo dados de telemetria
    de uma missão espacial e organizar essas informações em um dicionário.

    Parâmetro:
    caminho (str) -> caminho do arquivo CSV

    Retorno:
    dados (dict) -> dicionário com listas organizadas por tipo de dado
    """

    # Criação do dicionário que armazenará os dados organizados
    # Cada chave representa uma variável da missão
    # Cada valor é uma lista que armazenará os dados ao longo do tempo
    dados = {
        "horas": [],          # Horários das medições
        "geracao": [],        # Energia gerada (kWh)
        "consumo": [],        # Energia consumida (kWh)
        "reserva": [],        # Energia armazenada (kWh)
        "temperatura": [],    # Temperatura interna (°C)
        "radiacao": [],       # Nível de radiação
        "comunicacao": []     # Qualidade da comunicação (%)
    }

    # Abre o arquivo CSV no modo leitura
    # newline='' evita problemas com quebra de linha
    # encoding='utf-8' garante compatibilidade com caracteres especiais
    with open(caminho, newline='', encoding='utf-8') as csvfile:

        # DictReader lê cada linha como um dicionário
        # As chaves são os nomes das colunas do CSV
        leitor = csv.DictReader(csvfile)

        # Percorre cada linha do arquivo CSV
        for linha in leitor:

            # Adiciona os dados de cada coluna nas listas correspondentes

            # Armazena o horário (string)
            dados["horas"].append(linha["hora"])

            # Conversão para float (número decimal)
            # Isso é necessário para permitir cálculos depois

            dados["geracao"].append(float(linha["geracao_kwh"]))       # Energia gerada
            dados["consumo"].append(float(linha["consumo_kwh"]))       # Energia consumida
            dados["reserva"].append(float(linha["reserva_kwh"]))       # Energia armazenada
            dados["temperatura"].append(float(linha["temp_interna"]))  # Temperatura interna
            dados["radiacao"].append(float(linha["radiacao"]))         # Radiação
            dados["comunicacao"].append(float(linha["qualidade_comunicacao"]))  # Comunicação

    # Retorna o dicionário com todos os dados organizados
    return dados