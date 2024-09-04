import array as arr

vetores = arr.array('i',[0] * 6)

for x in range(len(list(vetores))):
    vetores[x] = int(input(f'Informe um número par para a posição {x}: '))
    while vetores[x] % 2 != 0:
        print('O número informado não é par')
        vetores[x] = int(input(f'Informe um número par para a posição {x}: '))

print('Vetores pares em ordem inversa: ')

for x in range(len(list(vetores))-1,-1,-1):
    print(vetores[x])