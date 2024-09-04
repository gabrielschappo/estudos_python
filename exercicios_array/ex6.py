import array as arr

posicoes = arr.array('f',[0] * 10)
for x in range(len(list(posicoes))):
    posicoes[x] = int(input(f'Informe a posição {x}: '))

maior = posicoes[0]
menor = posicoes[0]

for x in range(len(list(posicoes))):
    if posicoes[x] > maior:
        maior = posicoes[x]
    elif posicoes[x] < menor:
        menor = posicoes[x]

print(f'maior: {maior}')
print(f'menor: {menor}')