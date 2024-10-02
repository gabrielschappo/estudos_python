matriz = [[0]*4,[0]*4]
for x in range(2):
    for y in range(4):
        matriz[x][y] = int(input(f'Informe o elemento ({x+1},{y+1}): '))
for x in range(len(matriz)):
    print(matriz[x])