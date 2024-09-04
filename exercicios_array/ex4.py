import array as arr

posicoes = arr.array('f',[0] * 8)
for x in range(8):
    posicoes[x] = int(input(f'Digite o valor da posição {x}: '))
x = int(input('Informe uma posição: '))
y = int(input('Informe outra posição: '))
soma = posicoes[x] + posicoes[y]
print(soma)