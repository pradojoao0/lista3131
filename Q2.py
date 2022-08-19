

def lerMatriz():
    m, ler_linha = [], input()
    while ler_linha:
        m.append([int(i) for i in ler_linha.split(" ") if i])
        ler_linha = input()
    return m
def escreverMatriz(m):
    for linha in m:
        print(*linha)



matrizA = lerMatriz()

linhasA = len(matrizA)
colunasA = len(matrizA[0])

multPreta = 1
multBranca = 1


for linha in range(0, linhasA):
    for coluna in range(0, colunasA):
        #Linha par
        if(linha % 2 == 0):
            if(coluna % 2 == 0):
                if(matrizA[linha][coluna] % 2 == 0):
                    multBranca *= matrizA[linha][coluna]
            else:
                if(matrizA[linha][coluna] % 2 == 0):
                    multPreta *= matrizA[linha][coluna]
        else:
            if(coluna % 2 == 0):
                if(matrizA[linha][coluna] % 2 == 0):
                    multPreta *= matrizA[linha][coluna]
            else:
                if(matrizA[linha][coluna] % 2 == 0):
                    multBranca *= matrizA[linha][coluna]

print(f"multiplicação pares na cor=1 é {multPreta}; e na outra cor é {multBranca}")

