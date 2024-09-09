import numpy as np

array = np.zeros((20))
y = -1

for x in range(len(list(array))):
    array[x] = int(input('Informe um número: '))

print(array)

#np.flip poderia ser utilizado
#np.flip(array)
for x in range(10):
    array[x],array[y] = array[y],array[x]
    y -= 1

print(array)

