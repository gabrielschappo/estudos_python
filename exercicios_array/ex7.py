import array as arr

vetor = arr.array('i',[0] * 10)

for x in range(len(list(vetor))):
    vetor[x] = int(input(f'Informe o número na posição {x}: '))

maior = vetor[0]

for x in range(len(list(vetor))):
    if vetor[x] > maior:
        maior = vetor[x]
        pos = x

print(f'Maior elemento: {maior}')
print(f'Posição: {x}')
