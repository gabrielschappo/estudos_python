import array as arr

posicoes = arr.array('f',[0] * 10)
for x in range(10):
    posicoes[x] = int(input(f'Informe a posição {x}: '))

contador = 0

for x in range(10):
    if posicoes[x] % 2 == 0:
        contador += 1
        print(f'{posicoes[x]} é par')

print(f'{contador} número(s) é(são) par(es)')