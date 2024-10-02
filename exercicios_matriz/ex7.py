ordem = int(input('Informe a ordem da matriz: '))
matriz = []

for x in range(ordem):
    linha = []
    for y in range(ordem):
        if x == y:
            linha.append(1)
        else:
            linha.append(0)
    matriz.append(linha)

for i in range(len(matriz)):
    print(matriz[i])