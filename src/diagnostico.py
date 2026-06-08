def diagnostico(dados):
    reserva = dados["reserva"][-1]
    comunicacao = dados["comunicacao"][-1]
    radiacao = dados["radiacao"][-1]

    energia_baixa = reserva < 520
    comunicacao_ruim = comunicacao < 50
    radiacao_alta = radiacao > 8

    if energia_baixa and comunicacao_ruim and radiacao_alta:
        return "CRÍTICO"
    elif energia_baixa or comunicacao_ruim or radiacao_alta:
        return "ALERTA"
    else:
        return "NORMAL"
    