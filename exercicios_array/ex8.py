import array as arr

valores = arr.array('i', [0] * 6)

for x in range(len(list(valores))):
    valores[x] = int(input(f'Informe o valor na posição {x}: '))

print('Valores em ordem inversa:')

for x in range(len(list(valores))-1,-1,-1):
    print(valores[x])