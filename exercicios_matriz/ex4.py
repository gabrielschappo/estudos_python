a = [[2,-3],[-1,4]]
oposta = [[0]*2,[0]*2]

for x in range(2):
    for y in range(2):
        oposta[x][y] = a[x][y] * -1

print(f'A matriz oposta de A é: \n{oposta[0]}\n{oposta[1]}')