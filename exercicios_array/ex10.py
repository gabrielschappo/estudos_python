import array as arr

notas = arr.array('f',[0] * 15)
soma = 0

for x in range(len(list(notas))):
    notas[x] = float(input(f'Informe a nota do aluno {x+1}: '))
    while notas[x] > 10 or notas[x] < 0:
        print('Valor inválido')
        notas[x] = float(input(f'Informe a nota do aluno {x+1}: '))
    soma += notas[x]

media = soma / len(list(notas))
print(f'A média geral da turma é: {media:.2f}')