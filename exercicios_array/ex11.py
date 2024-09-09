import array as arr

vetor = arr.array('f',[0] * 10)
neg = 0
soma = 0

for x in range(len(list(vetor))):
    vetor[x] = float(input(f'Informe o número de posição {x}: '))
    if vetor[x] < 0:
        neg += 1
    else:
        soma += vetor[x]

print(f'Esse vetor possui {neg} números negativos\nA soma dos números positivos é igual a: {soma}')
