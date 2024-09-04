import array as arr

numeros = arr.array('f',[0.0] * 10)
for x in range(10):
    numeros[x] = float(input('Digite um número: '))

quadrados = arr.array('f', [0.0] * 10)
for x in range(10):
    quadrados[x] = numeros[x] ** 2

print(f'Conjunto original: {numeros}')
print(f'Conjunto ao quadrado: {quadrados}')