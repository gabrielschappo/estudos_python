matriz = [[0,1,2,3,4,5,6,7],
          [1,0,2,11,6,15,11,1],
          [2,2,0,7,12,4,2,15],
          [3,11,7,0,11,8,3,13],
          [4,6,12,11,0,10,2,1],
          [5,15,4,8,10,0,5,13],
          [6,11,2,3,2,5,0,14],
          [7,1,15,13,1,13,14,0]]

cidade1 = int(input('Informe a cidade de partida: '))
cidade2 = int(input('Informe a cidade de destino: '))

tempo = matriz[cidade1][cidade2]
print(f'Tempo do trajeto: {tempo}')

rota = []
trajeto = 0
cidade = 1

while cidade != 0:
    cidade = int(input('Informe uma cidade (digite 0 para encerrar): '))
    if cidade != 0:
        rota.append(cidade)

for x in range(len(rota)-1):
    trajeto += matriz[rota[x]][rota[x+1]]

print(f'Rota total: {rota}')
print(f'Tempo do trajeto: {trajeto}')
