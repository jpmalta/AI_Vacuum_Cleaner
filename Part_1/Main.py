# # Prática 03 - Agentes Inteligentes
# ## Agente Reativo Simples: Robô Aspirador de Pó

#Nome: João Pedro Costa Malta RA: 23002743

import time
from random import randint, choice

def mostrar_na_tela(ambiente):
    for linha in ambiente:
        print(linha)
    print("\n")

#Problema atual: ele mostra apenas a posição do aspirador onde está sujo
#O que fazer para arrumar: definir o caminho que ele deve seguir para chegar na próxima sala suja, e mostrar a posição do aspirador nas salas limpas que ele tiver que atravessar até lá

def aspirador(ambiente):
    linha_atual, coluna_atual = randint(0, 2), randint(0, 2) 
    while True: 
        if ambiente[linha_atual][coluna_atual] == 'sujo':
            ambiente[linha_atual][coluna_atual] = 'A'
            mostrar_na_tela(ambiente)    
            time.sleep(0.5)
            ambiente[linha_atual][coluna_atual] = 'limpo'
            
        if all(all(sala == 'limpo' for sala in linha) for linha in ambiente):
            print("Todas as salas estão limpas")
            break
    
        movimentos = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        movimentos_validos = [(linha_atual + dx, coluna_atual + dy) for dx, dy in movimentos 
                               if 0 <= linha_atual + dx < 3 and 0 <= coluna_atual + dy < 3]
        
        if movimentos_validos:
            linha_atual, coluna_atual = choice(movimentos_validos)

    return ambiente

ambiente = [[choice(['sujo', 'limpo']) for _ in range(3)] for _ in range(3)]
mostrar_na_tela(aspirador(ambiente))
