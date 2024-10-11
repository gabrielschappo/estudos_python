grade = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
rodada = 0

def jogada(rodada):
    if rodada % 2 == 0:
        simbolo = 'X'
    else:
        simbolo = 'O'
    print('\n  1 2 3')
    for x in range(3):
        print(f'{x+1} {grade[x][0]} {grade[x][1]} {grade[x][2]}')
    print(f'\nJogada do {simbolo}: ')
    rodada += 1
    linha = int(input('\nDigite a linha: ')) - 1
    coluna = int(input('Digite a coluna: ')) - 1
    while grade[linha][coluna] != ' ':
        print('Posição já utilizada')
        linha = int(input('\nDigite a linha: '))
        coluna = int(input('Digite a coluna: '))
    grade[linha][coluna] = simbolo
    verificar(rodada)

def verificar(rodada):
    fim = 0
    for x in range(3):
        if (grade[x] == ['X','X','X']) or (grade[0][x] == 'X' and grade[1][x] == 'X' and grade[2][x] == 'X'):
            fim = 1
            vitoriax()
        elif (grade[x] == ['O','O','O']) or (grade[0][x] == 'O' and grade[1][x] == 'O' and grade[2][x] == 'O'):
            fim = 1
            vitoriao()
    if (grade[0][0] == 'X' and grade[1][1] == 'X' and grade[2][2] == 'X') or (grade[0][2] == 'X' and grade[1][1] == 'X' and grade[2][0] == 'X'):
        vitoriax()
    elif (grade[0][0] == 'O' and grade[1][1] == 'O' and grade[2][2] == 'O') or (grade[0][2] == 'O' and grade[1][1] == 'O' and grade[2][0] == 'O'):
        vitoriao()
    elif grade[0][0] != ' ' and grade[0][1] != ' ' and grade[0][2] != ' ' and grade[1][0] != ' ' and grade[1][1] != ' ' and grade[1][2] != ' ' and grade[2][0] != ' ' and grade[2][1] != ' ' and grade[2][2] != ' ':
        print('\nDeu velha!')
    elif fim == 0:
        jogada(rodada) 

def vitoriax():
    print('\n  1 2 3')
    for x in range(3):
        print(f'{x+1} {grade[x][0]} {grade[x][1]} {grade[x][2]}')
    print('\nVitória X!\n')

def vitoriao():
    print('\n  1 2 3')
    for x in range(3):
        print(f'{x+1} {grade[x][0]} {grade[x][1]} {grade[x][2]}')
    print('\nVitória O!\n')   

jogada(rodada)
