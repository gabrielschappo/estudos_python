ordem = int(input('Informe a ordem do triângulo de Pascal: '))
triangulo = []

for x in range(ordem):
    linha = []
    for y in range(ordem):
        if x == y or y == 0:
            linha.append(1)
        elif len(linha) != x+1:
            linha.append(triangulo[x-1][y-1] + triangulo[x-1][y])
    triangulo.append(linha)

for i in range(len(triangulo)):
    print(triangulo[i])