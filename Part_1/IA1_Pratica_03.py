#!/usr/bin/env python
# coding: utf-8

# # Prática 03 - Agentes Inteligentes
# 
# ## Agente Reativo Simples: Robô Aspirador de Pó

# In[ ]:


# Bibliotecas necessarias

import time
from random import randint


# In[ ]:


# Definindo variaveis

agente = 'A'

limpo = 'limpo'

ambiente = [['sujo', 'sujo', 'sujo']]


# In[ ]:


def mostrar_na_tela(ambiente):
    
    for sala in ambiente:
        
        print(sala)
        
    print("\n")    


# In[ ]:


def aspirador(ambiente):
    
    atual = randint(0, 2)
    
    while(True):
        
        if ambiente[0][atual] != limpo:
                
            ambiente[0][atual] = agente
                
            mostrar_na_tela(ambiente)
            time.sleep(0.5)
                
            ambiente[0][atual] = limpo
                
            if atual == 0 and ambiente[0][atual + 1] != limpo:
                
                atual = atual + 1
                    
            elif atual == 0 and ambiente[0][atual + 1] == limpo and ambiente[0][atual + 2] == limpo:
                    
                print("Todas as salas estão limpas")
                break
                    
            elif atual == 0 and ambiente[0][atual + 1] == limpo and ambiente[0][atual + 2] != limpo:
                    
                atual = atual + 1    
                    
            elif atual == 1 and ambiente[0][atual - 1] != limpo and ambiente[0][atual + 1] == limpo:
                
                atual = atual - 1
                    
            elif atual == 1 and ambiente[0][atual - 1] == limpo and ambiente[0][atual + 1] != limpo:
                
                atual = atual + 1
                
            elif atual == 1 and ambiente[0][atual - 1] != limpo and ambiente[0][atual + 1] != limpo:
                
                atual = atual - 1
                    
            elif atual == 1 and ambiente[0][atual - 1] == limpo and ambiente[0][atual + 1] == limpo:
                    
                print("Todas as salas estão limpas")
                break
                    
            elif atual == 2 and ambiente[0][atual - 1] != limpo:
                    
                atual = atual - 1
                    
            elif atual == 2 and ambiente[0][atual - 1] == limpo and ambiente[0][atual - 2] == limpo:
                    
                print("Todas as salas estão limpas")
                break
                
        else:
                
            salva_estado = ambiente[0][atual]
                
            ambiente[0][atual] = agente
                
            mostrar_na_tela(ambiente)
            time.sleep(0.5)
                
            ambiente[0][atual] = salva_estado
                
            if atual == 0 and ambiente[0][atual + 1] != limpo:
                
                atual = atual + 1
                    
            elif atual == 0 and ambiente[0][atual + 1] == limpo and ambiente[0][atual + 2] == limpo:
                    
                print("Todas as salas estão limpas")
                break
                    
            elif atual == 0 and ambiente[0][atual + 1] == limpo and ambiente[0][atual + 2] != limpo:
                    
                atual = atual + 1    
                    
            elif atual == 1 and ambiente[0][atual - 1] != limpo and ambiente[0][atual + 1] == limpo:
                
                atual = atual - 1
                    
            elif atual == 1 and ambiente[0][atual - 1] == limpo and ambiente[0][atual + 1] != limpo:
                
                atual = atual + 1
                
            elif atual == 1 and ambiente[0][atual - 1] == limpo and ambiente[0][atual + 1] != limpo:
                
                atual = atual - 1
                    
            elif atual == 1 and ambiente[0][atual - 1] != limpo and ambiente[0][atual + 1] == limpo:
                    
                print("Todas as salas estão limpas")
                break
                    
            elif atual == 2 and ambiente[0][atual - 1] != limpo:
                    
                atual = atual - 1
                    
            elif atual == 2 and ambiente[0][atual - 1] == limpo and ambiente[0][atual - 2] == limpo:
                    
                print("Todas as salas estão limpas")
                break
                
            continue
                
    return ambiente


# In[ ]:


mostrar_na_tela(aspirador(ambiente))

