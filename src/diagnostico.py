def diagnostico(dados):
    # Obtém os valores mais recentes de cada variável.
    # O índice [-1] representa o último elemento da lista.

    reserva = dados["reserva"][-1]           # Energia disponível (kWh)
    comunicacao = dados["comunicacao"][-1]   # Qualidade da comunicação (%)
    radiacao = dados["radiacao"][-1]         # Nível de radiação

    # Conversão dos valores para condições booleanas, tornando-as mais fáceis de usar em diagnósticos.

    energia_baixa = reserva < 520
    # True se a reserva energética estiver abaixo de 520 kWh

    comunicacao_ruim = comunicacao < 50
    # True se a qualidade da comunicação estiver abaixo de 50%

    radiacao_alta = radiacao > 8
    # True se a radiação estiver acima do limite seguro

    # Utilização do operador NOT.
    # ESTÁVEL: O sistema só é considerado estável quando nenhum problema é detectado.
    sistema_estavel = (
        not energia_baixa and
        not comunicacao_ruim and
        not radiacao_alta
    )
    # DIAGNÓSTICO PRINCIPAL
    # CRÍTICO:Todos os problemas acontecem ao mesmo tempo.
    if energia_baixa and comunicacao_ruim and radiacao_alta:
        return "CRÍTICO"
    # ALERTA: Pelo menos um dos problemas foi detectado.
    elif energia_baixa or comunicacao_ruim or radiacao_alta:
        return "ALERTA"
    # NORMAL: Nenhum problema foi encontrado.
    elif sistema_estavel:
        return "NORMAL"