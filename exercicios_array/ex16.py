import numpy as np

n = int(input('Quantos elementos o vetor A terá: '))
a = np.zeros((n))
m = int(input('Quantos elementos o vetor B terá: '))
b = np.zeros((m))

for x in range(n):
    a[x] = float(input(f'Informe o valor do item {x} de A: '))

a = sorted(a)

for x in range(m):
    b[x] = float(input(f'Informe o valor do item {x} de B: '))

b = sorted(b)
c = np.concatenate((a,b))
c = sorted(c)
for x in range(len(list(c))):
    print(c[x])