# Criando uma função para gerar alertas com base nos dados de telemetria
def gerar_alertas(dados):
    # Lista vazia para armazenar os alertas gerados
    alertas = []
# Obtém os valores mais recentes de cada variável.
    reserva = dados["reserva"][-1]           # Energia disponível (kWh)
    comunicacao = dados["comunicacao"][-1]   # Qualidade da comunicação (%)
    radiacao = dados["radiacao"][-1]         # Nível de radiação
    temperatura = dados["temperatura"][-1]   # Temperatura interna (°C)

# ALERTAS DE ENERGIA
    if reserva < 500:
        alertas.append("ALERTA: Reserva energética crítica!")
    elif reserva < 520:
        alertas.append("AVISO: Reserva energética baixa.")
    elif reserva < 550:
        alertas.append("ATENÇÃO: Reserva energética abaixo do ideal.")  
    else:
        alertas.append("Reserva energética dentro dos parâmetros normais.")

# ALERTAS DE COMUNICAÇÃO
    if comunicacao < 40:
        alertas.append("ALERTA: Comunicação crítica!")
    elif comunicacao < 50:
        alertas.append("AVISO: Comunicação ruim.")
    elif comunicacao < 70:
        alertas.append("ATENÇÃO: Comunicação abaixo do ideal.")
    else:
        alertas.append("Comunicação dentro dos parâmetros normais.")

# ALERTAS DE RADIAÇÃO
    if radiacao > 8:
        alertas.append("ALERTA: Radiação crítica!")
    elif radiacao > 6:
        alertas.append("AVISO: Radiação alta.")
    elif radiacao > 4:
        alertas.append("ATENÇÃO: Radiação acima do ideal.")
    else:
        alertas.append("Radiação dentro dos parâmetros normais.")

# ALERTAS DE TEMPERATURA
    if temperatura > 30:
        alertas.append("ALERTA: Temperatura crítica!")
    elif temperatura > 28:
        alertas.append("AVISO: Temperatura alta.")
    elif temperatura > 26:
        alertas.append("ATENÇÃO: Temperatura acima do ideal.")
    else:
        alertas.append("Temperatura dentro dos parâmetros normais.")

# ALERTA COMBINADO
    if reserva < 500 and comunicacao < 40 and radiacao > 8 and temperatura > 30:
        alertas.append("ALERTA CRÍTICO: Múltiplos sistemas em situação crítica!")
    elif reserva < 520 or comunicacao < 50 or radiacao > 6 or temperatura > 28:
        alertas.append("ALERTA: Múltiplos sistemas com problemas detectados.")
    elif reserva < 550 or comunicacao < 70 or radiacao > 4 or temperatura > 26:
        alertas.append("AVISO: Múltiplos sistemas abaixo do ideal.")
    else: 
        alertas.append("Todos os sistemas dentro dos parâmetros normais.")

# Retorna a lista de alertas para o sistema principal
    return alertas