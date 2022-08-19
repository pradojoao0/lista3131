import numpy as np

def lerMatriz():
    m, ler_linha = [], input()
    while ler_linha: 
        m.append([int(i) for i in ler_linha.split(" ") if i])
        ler_linha = input()
    return m 
def escreverMatriz(m):
    for linha in m:
        print(*linha)
        
        
m = lerMatriz()

linhas = len(m)
colunas = len(m[0])

gotcha = False

if(colunas > 0):
    
    for l in range(0, linhas):
        if(gotcha == False):
            for c in range(0, colunas):
                if(m[l][0] == 5):
                    print(l)
                    gotcha = True
                    break
        else:
            break
                    
                
            
    if(gotcha == False):
        print("-1")
            
else:
    print("-1")
