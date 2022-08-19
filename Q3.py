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
        
        
entrada = input().split(" ")
linha = int(entrada[0])
coluna = int(entrada[1])



m = np.zeros((linha ,coluna), dtype=int)



for linhas in range(0, linha):
    for colunas in range(0, coluna):
        m[linhas][colunas] = (2*linhas + 2*colunas) % 9
escreverMatriz(m)
