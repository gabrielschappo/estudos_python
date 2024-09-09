import numpy as np

n = int(input('Quantos elementos você deseja informar: '))
lista = np.zeros((n))
pares = 0
impar = 0

for x in range(len(list(lista))):
    lista[x] = int(input('Informe um número: '))
    if lista[x] % 2 == 0:
        pares += 1
    else:
        impar += 1

lista_par = np.zeros((pares))
lista_impar = np.zeros((impar))
p = 0
i = 0

#possibilidade:
#lista_par = sorted(filter(lambda x: x % 2 == 0, lista))
for x in range(len(list(lista))):
    if lista[x] % 2 == 0:
        lista_par[p] = lista[x]
        p += 1
    else:
        lista_impar[i] = lista[x]
        i += 1

print(f'original: {lista}')
print(f'pares: {lista_par}')
print(f'impares: {lista_impar}')