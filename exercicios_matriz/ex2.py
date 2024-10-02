matriz = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
soma_primeira_col = 0
prod_primeira_linha = 1
soma_total = 0
prod_diagonal_principal = 1

for x in range(4):
    soma_primeira_col += matriz[x][0]
print(f'A soma da primeira coluna é: {soma_primeira_col}')

for x in range(4):
    prod_primeira_linha *= matriz[0][x]
print(f'O produto da primeira linha é: {prod_primeira_linha}')

for x in range(4):
    for y in range(4):
        soma_total += matriz[x][y]
print(f'A soma de todos elementos da matriz é: {soma_total}')

for x in range(4):
    prod_diagonal_principal *= matriz[x][x]
print(f'O produto da diagonal principal é: {prod_diagonal_principal}')
