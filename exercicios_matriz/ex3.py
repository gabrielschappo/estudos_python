a = [[-10,1,4,6],[2,3,2,8]]
b = [[1,8,4,-1],[0,6,3,-3]]
c = [[0]*4,[0]*4]

for x in range(2):
    for y in range(4):
        c[x][y] = a[x][y] + b[x][y]

print(f'A soma das matrizes A e B é: \n{c[0]}\n{c[1]}')
