## Sistema Inteligente de Monitoramento de Missão Espacial

O SIMME é uma aplicação desenvolvida em Python para simular o monitoramento operacional de uma missão espacial experimental.

O sistema:

monitora dados de telemetria da missão;
identifica situações de alerta e criticidade;
detecta inconsistências nos dados;
gera alertas automáticos;
realiza previsão energética;
fornece recomendações para a continuidade da operação.
Funcionalidades
Leitura e interpretação dos dados

No arquivo leitordados.py, os dados de telemetria são lidos a partir de um arquivo CSV e organizados em estruturas.

Os dados monitorados incluem:

geração de energia;
consumo de energia;
reserva energética;
temperatura interna;
nível de radiação;
qualidade da comunicação.
Diagnóstico da missão

## Diagnóstico da Missão

No arquivo `diagnostico.py`, o sistema analisa reserva energética, comunicação e radiação para classificar a missão como NORMAL, ALERTA ou CRÍTICO, utilizando operadores booleanos (AND, OR e NOT).

Também é realizada a detecção de inconsistências entre os módulos e os dados de telemetria.

---

## Alertas Automáticos

No arquivo `alertas.py`, são gerados alertas classificados em ALERTA CRÍTICO, ALERTA, AVISO e ATENÇÃO, exibidos por ordem de prioridade.

---

## Previsão Energética

No arquivo `previsao.py`, é utilizada a técnica de Média Móvel Simples com os três últimos ciclos de consumo para estimar a reserva energética futura.

---

## Estruturas de Dados

O arquivo `estruturas.py` utiliza:

Dicionário (Hash):módulos críticos;
- Fila (Queue): alertas priorizados;
- Pilha (Stack): histórico de eventos;
- Hierarquia (Árvore): organização dos subsistemas;
- Matriz: dados de telemetria do CSV.

---

## Recomendações Automáticas

O sistema pode recomendar:

- economia de energia;
- comunicação de emergência;
- suspensão de atividades externas.

---


# Exemplo de saída
STATUS DA MISSÃO: CRÍTICO

ALERTAS GERADOS:
- ALERTA: Radiação crítica
- AVISO: Comunicação ruim
- AVISO: Temperatura alta

PREVISÃO ENERGÉTICA:
Reserva prevista para o próximo ciclo: 501.67 kWh

## Como Executar

```bash
cd src
python sistema.py

---

Integrantes
Nome: ANA CAROLINA FREIRE MAFRA – rm573650
Nome: Daniel Guimarães Barreto – rm573425
Nome: Paulo Henrique da Silva Gola – rm572992
Nome: Vinicius Daniel de Borba – rm572091
Nome: Vitor de Araujo Ferreira – rm572838

---

Vídeo de Apresentação:
Link do vídeo:

[Youtube]

Link do repositório:
(https://github.com/viniciusdanield/Projeto-Missao-Espacial-GS.git)
