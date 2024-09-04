import numpy as np

matriculas = np.zeros((100))

for x in range(len(list(matriculas))):
    num = int(input(f'Informe a matrícula do aluno {x}: '))
    if num in matriculas:
        print('Matricula ja presente na lista!')
    else:
        matriculas[x] = num