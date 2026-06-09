# SISTEMA PRINCIPAL

# Importação dos módulos do projeto

from leitordados import carregar_dados #função não está sendo chamada 
from diagnostico import diagnostico
from previsao import previsao
from alertas import gerar_alertas
from estruturas import (
    modulos,
    fila_alertas,
    pilha_eventos,
    hierarquia
)

# LEITURA DOS DADOS

dados = carregar_dados("../data/dados.csv")

# DIAGNÓSTICO DA MISSÃO

status = diagnostico(dados)

# GERAÇÃO DE ALERTAS

alertas = gerar_alertas(dados)

# Adiciona os alertas na fila

for alerta in alertas:
    fila_alertas.append(alerta)

# PREVISÃO DE ENERGIA

media_consumo, reserva_prevista = previsao(dados)

# EXIBIÇÃO DOS RESULTADOS

print(" SISTEMA DE MONITORAMENTO ESPACIAL")

# STATUS DA MISSÃO

print("\nSTATUS DA MISSÃO:")
print(status)

# ALERTAS

print("\nALERTAS GERADOS:")

if len(fila_alertas) == 0:
    print("Nenhum alerta encontrado.")

else:
    for alerta in fila_alertas:
        print("-", alerta)

# PREVISÃO ENERGÉTICA

print("\nPREVISÃO ENERGÉTICA:")

print(
    f"Consumo médio dos últimos ciclos: "
    f"{media_consumo:.2f} kWh"
)

print(
    f"Reserva prevista para o próximo ciclo: "
    f"{reserva_prevista:.2f} kWh"
)

# RECOMENDAÇÕES AUTOMÁTICAS

print("\nRECOMENDAÇÕES:")

if reserva_prevista < 510:
    print("- Ativar modo de economia de energia.")

if dados["comunicacao"][-1] < 50:
    print("- Ativar comunicação de emergência.")

if dados["radiacao"][-1] > 8:
    print("- Suspender atividades externas.")

# ESTRUTURAS UTILIZADAS

print("\nMÓDULOS CRÍTICOS:")

for modulo, status_modulo in modulos.items():

    estado = "OK" if status_modulo == 1 else "FALHA"

    print(f"{modulo}: {estado}")

# PILHA DE EVENTOS

print("\nÚLTIMOS EVENTOS:")

for evento in pilha_eventos:
    print("-", evento)

# HIERARQUIA DA MISSÃO

print("\nHIERARQUIA DA MISSÃO:")
print(hierarquia)

print(" FIM DA EXECUÇÃO")
