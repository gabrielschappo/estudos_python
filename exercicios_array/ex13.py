import numpy as np

candidatos = int(input('Informe o número de candidatos: '))
votantes = int(input('Informe o número de votantes: '))

votos = np.zeros((candidatos))

for x in range(votantes):
    voto = int(input('Digite o número do candidato: '))
    votos[voto-1] += 1

for x in range(candidatos):
    print(f'Votos candidato {x+1}: {votos[x]}')