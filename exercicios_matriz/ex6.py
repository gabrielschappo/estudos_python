a = [[2,3,1],[-1,0,2]]
b = [[1,-2],[0,5],[4,1]]
axb = [[0]*2,[0]*2]

for x in range(len(a)):
    for y in range(len(b[0])):
        for i in range(len(b)):
            axb[x][y] += a[x][i] * b[i][y]

print('O resultado da matriz A x B é:')
print(axb[0])
print(axb[1])
        