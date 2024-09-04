import numpy as np

notas = np.array([9.9, 9.7, 9.8, 10, 10])

notas = np.delete(notas, np.argmax(notas))
notas = np.delete(notas, np.argmin(notas))
soma = 0

for x in range(len(notas)):
    soma += notas[x]
    
media = soma / len(notas)
print(f'A média final é: {media}')