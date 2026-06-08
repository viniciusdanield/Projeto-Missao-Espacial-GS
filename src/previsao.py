def previsao(dados):
    # Obtém as listas de geração, consumo e reserva
    geracao = dados["geracao"]     # Energia gerada (kWh)
    consumo = dados["consumo"]     # Energia consumida (kWh)
    reserva = dados["reserva"]     # Energia armazenada (kWh)
# Calcular a média movel utilizando os últimos 3 valores de consumo de energia
    media_consumo = (
    consumo[-1] +  # Consumo mais recente
    consumo[-2],  # Consumo anterior
    consumo[-3]   # Consumo antes do anterior
) / 3 # Dividir pela quantidade de valores para obter a média

# Obtém os valores mais recentes
    geracao_atual = geracao[-1]  # Energia gerada mais recente
    reserva_atual = reserva[-1]  # Energia armazenada mais recente

# Previsão energética para o proximo ciclo
# Se o consumo continuar seguindo a média dos ultimos periodos, estima-se a nova reserva
    reserva_prevista = reserva_atual + geracao_atual - media_consumo

# Retorna os resultados para o sistema principal
    return media_consumo, reserva_prevista


