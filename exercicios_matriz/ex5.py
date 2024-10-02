a = [[-7,8],[4,9],[2,1]]
a_transposta = [[0]*3,[0]*3]

for i in range(len(a_transposta)):
    for x in range(len(a)):
        a_transposta[i][x] = a[x][i]

print('A matriz transposta de A é:')        
print(a_transposta[0])
print(a_transposta[1])