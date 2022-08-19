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


matriz = lerMatriz();

colunas = len(matriz[0])
linhas = len(matriz)

##Definir a linha do meio 

cont = 0

for linha in range(0, len(matriz)):
    for coluna in range(0, len(matriz[linha])):
        if(coluna >= linha):
            break
        else:
            if(matriz[linha][coluna] % 2 != 0):
                cont = cont+matriz[linha][coluna]

print(f"soma abaixo ímpares = {cont}")
