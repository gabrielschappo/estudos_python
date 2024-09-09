import numpy as np

matriculas = np.zeros((100))

for x in range(len(list(matriculas))):
    num = int(input(f'Informe a matrícula do aluno {x}: '))
    while num in matriculas:
        print('Matricula ja presente na lista!')
        num = int(input(f'Informe a matrícula do aluno {x}: '))
    matriculas[x] = num