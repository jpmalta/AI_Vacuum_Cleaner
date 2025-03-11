# # Prática 03 parte 02 - Agentes Inteligentes
# ## Agente Reativo Simples: Robô Aspirador de Pó

#Nome: João Pedro Costa Malta RA: 23002743

#Questão 1) Na Prática 03, foi implementado um Agente Aspirador de Pó para um ambiente 3×3, onde as salas
#limpas e sujas, bem como a posição inicial do agente, eram definidas aleatoriamente. Agora, expandiremos essa
#abordagem para avaliar a eficiência do Aspirador de Pó na limpeza. Para isso, consideremos os seguintes pontos:

import time
from random import choice
import math
import copy

def mostrar_na_tela(ambiente):
    for linha in ambiente:
        print(linha)
    print("\n")

def criar_ambiente(tamanho=5):
    return [[choice(['sujo', 'limpo']) for _ in range(tamanho)] for _ in range(tamanho)]

def aspirador(ambiente, nome_agente="Agente A"):
    linha_atual, coluna_atual = (2, 2)
    mostrar_na_tela(ambiente)
    while True: 
        if ambiente[linha_atual][coluna_atual] == 'sujo':
            ambiente[linha_atual][coluna_atual] = nome_agente[0]
            time.sleep(0.5)
            mostrar_na_tela(ambiente)
            ambiente[linha_atual][coluna_atual] = 'limpo'
        
        mostrar_na_tela(ambiente)

        if all(all(sala == 'limpo' for sala in linha) for linha in ambiente):
            print(f"Todas as salas estão limpas pelo {nome_agente}")
            break
    
        movimentos = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        movimentos_validos = [(linha_atual + dx, coluna_atual + dy) for dx, dy in movimentos 
                               if 0 <= linha_atual + dx < len(ambiente) and 0 <= coluna_atual + dy < len(ambiente[0])]
        
        if movimentos_validos:
            linha_atual, coluna_atual = choice(movimentos_validos)

    return ambiente

def aspirador_euclidiano(ambiente, nome_agente="Agente B"):
    linha_atual, coluna_atual = (2, 2)
    mostrar_na_tela(ambiente)
    
    while True:
        if ambiente[linha_atual][coluna_atual] == 'sujo':
            ambiente[linha_atual][coluna_atual] = nome_agente[0]
            time.sleep(0.5)
            mostrar_na_tela(ambiente)
            ambiente[linha_atual][coluna_atual] = 'limpo'

        if all(all(sala == 'limpo' for sala in linha) for linha in ambiente):
            print(f"Todas as salas estão limpas pelo {nome_agente}")
            break

        # Encontrar todas as células sujas no ambiente
        celulas_sujas = [(i, j) for i in range(len(ambiente)) for j in range(len(ambiente[i])) if ambiente[i][j] == 'sujo']

        if celulas_sujas:
            # Escolher a célula suja mais próxima com base na distância Euclidiana
            linha_alvo, coluna_alvo = min(celulas_sujas, key=lambda pos: math.sqrt((pos[0] - linha_atual)**2 + (pos[1] - coluna_atual)**2))

            # Determinar o melhor movimento na direção da célula suja mais próxima
            movimentos = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            movimentos_validos = [(linha_atual + dx, coluna_atual + dy) for dx, dy in movimentos
                                   if 0 <= linha_atual + dx < len(ambiente) and 0 <= coluna_atual + dy < len(ambiente[0])]

            if movimentos_validos:
                linha_atual, coluna_atual = min(movimentos_validos, key=lambda pos: math.sqrt((pos[0] - linha_alvo)**2 + (pos[1] - coluna_alvo)**2))
        
        mostrar_na_tela(ambiente)

    return ambiente

# Criação do ambiente
ambiente_inicial = criar_ambiente()

# Execução do Agente A
print("Execução do Agente A:")
ambiente_para_agente_a = copy.deepcopy(ambiente_inicial)
mostrar_na_tela(aspirador(ambiente_para_agente_a))

# Execução do Agente B
print("Execução do Agente B:")
ambiente_para_agente_b = copy.deepcopy(ambiente_inicial)
mostrar_na_tela(aspirador_euclidiano(ambiente_para_agente_b))