from collections import deque
# DICIONÁRIO (HASH)
# Armazena o status dos módulos críticos da missão.
# 1 = Funcionando
# 0 = Falha

modulos = {
    "suporte_vida": 1,
    "energia": 1,
    "comunicacao": 0,
    "habitat": 1,
    "laboratorio": 1,
    "armazenamento": 1
}
# FILA (QUEUE)
# Armazena alertas por ordem de chegada.
# O primeiro alerta inserido será o primeiro removido.

fila_alertas = deque()
# PILHA (STACK)
# Armazena os últimos eventos da missão.
# O último evento inserido fica no topo da pilha.

pilha_eventos = [
    "Sistema iniciado",
    "Painel solar ajustado",
    "Pico de consumo detectado",
    "Comunicação instável",
    "Reinicialização do sensor térmico",
    "Radiação acima do normal",
    "Modo economia ativado",
    "Alerta crítico de comunicação"
]
# HIERARQUIA DA MISSÃO (ÁRVORE SIMPLES)
# Representa a organização dos subsistemas.

hierarquia = {
    "energia": {
        "geracao": ["painel_solar"],
        "armazenamento": ["baterias"]
    },

    "habitat": {
        "suporte": ["oxigenio"],
        "ambiente": ["temperatura"],
        "comunicacao": ["antenas"]
    }
}

# FUNÇÃO PARA EXIBIR AS ESTRUTURAS

def mostrar_estruturas():
    print("\nSTATUS DOS MÓDULOS")
    for modulo, status in modulos.items():
        print(f"{modulo}: {status}")

    print("\nÚLTIMOS EVENTOS")
    for evento in pilha_eventos:
        print(evento)

    print("\nHIERARQUIA DA MISSÃO")
    print(hierarquia)