import random

cores = ['preto', 'vermelho']
moedas = 100
print('Bem vindo ao CASSINO!')
nome = input('\nDigite o seu nome: ')
print(f'\nBoa sorte {nome}!')

while True: 
  if moedas <= 0:
    print(f'\nVocê não tem mais moedas para jogar...\nObrigado por jogar no CASSINO!\nVolte sempre, {nome}.')
    break
  print('\nDigite 1 para jogar na roleta\nDigite 2 para jogar blackjack(21)\nDigite 0 para sair')
  jogar = int(input('O que quer jogar?'))
  if jogar == 0:
    print('\nObrigado por jogar no CASSINO!\nVolte sempre.')
    break
  while jogar == 1:
    print('\nROLETA')
    cor = input('Digite a cor que deseja apostar(preto ou vermelho): ')
    while cor.lower() != 'vermelho' and cor.lower() != 'preto':
      print('Cor inválida')
      cor = input('Digite a cor que deseja apostar(preto ou vermelho): ')
    print(f'\nVocê possui {moedas:.2f} moedas')
    valor = float(input('Digite o valor que deseja apostar: '))
    while valor > moedas:
      print('\nSaldo insuficiente!')
      print(f'Você possui {moedas:.2f} moedas')
      valor = float(input('Digite o valor que deseja apostar: '))
    quant = int(input('Digite quantas vezes quer apostar esse valor: '))
    while quant * valor > moedas:
      print(f'\nSaldo insuficiente\nVocê possui {moedas:.2f} moedas')
      valor = float(input('Digite o valor que deseja apostar: '))
      quant = int(input('Digite quantas vezes quer apostar esse valor: '))
    print(f'\nCor escolhida: {cor}\nValor da aposta: {valor}\nQuantidade de vezes que esse valor e essa cor serão apostados: {quant}')
    jogar = int(input('Digite 1 para confirmar a aposta ou 3 para voltar ao menu: '))
    print('\n')
    lucroi = moedas
    if jogar == 1:
      for x in range(quant):
        resultado_cor = random.choice(cores)
        print(f'Cor sorteada na roleta: {resultado_cor}')
        if resultado_cor == cor.lower():
          print(f'Acertou! +{valor:.2f}')
          moedas += valor
        else:
          print(f'Errou! -{valor:.2f}')
          moedas -= valor
      lucrof = moedas
      print(f'\nVocê possui {moedas:.2f} moedas!')
      if lucrof > lucroi:
        print(f'\nPARABÉNS\nVocê obteve {lucrof-lucroi} moedas de lucro!')
      elif lucrof < lucroi:
        print(f'\nQUE PENA!\nInfelizmente você perdeu {lucroi-lucrof} moedas!')
    jogar = 3

  while jogar == 2:
    print(f'\nVocê possui {moedas:.2f} moedas')
    valor = int(input("Quantas moedas deseja apostar?"))
    while valor > moedas:
      valor = int(input("MOEDAS INSUFICIENTES! Quantas moedas deseja apostar?"))
    cartas = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,'A','A','A','A']
    carta1 = random.choice(cartas)
    cartas.remove(carta1)
    carta2 = random.choice(cartas)
    cartas.remove(carta2)
    carta3 = random.choice(cartas)
    cartas.remove(carta3)
    soma1 = carta3
    soma2 = 0
    if carta3 == 'A':
      soma1 = 11
    if carta1 == 'A' and carta2 == 'A':
      soma2 = 12
    elif carta1 == 'A' or carta2 == 'A':
      if carta1 == 'A':
        soma2 = carta2 + 11
      elif carta2 == 'A':
        soma2 = carta1 + 11
    else:
      soma2 = carta1 + carta2
    decisao1 = 0
    decisao2 = 0
    print("\nA carta inicial do dealer é:",carta3)
    print("O baralho incial do dealer vale:",soma1)
    print("\nSuas cartas iniciais são:",carta1,"e",carta2)
    print("O seu baralho inicial vale:",soma2)

    while decisao1 != 2 and decisao1 != 3 and decisao1 != 4:
      print("\nSua vez!")
      decisao1 = int(input("Qual sua jogada?\n1- pedir carta\n2- parar\n3- abandonar\n"))
      if decisao1 == 1:
        resultado = random.choice(cartas)
        cartas.remove(resultado)
        if resultado == 'A':
          resultado = 11 if soma2 + 11 <= 21 else 1  
        print("A carta retirada por você vale: ",resultado)
        soma2 = soma2 + resultado
        print("Seu baralho atual vale: ",soma2)
        print("Fim de rodada")
        print("________________________________________________________________")
        if soma2 == 21:
          decisao1 = 2
        if soma2 > 21:
          decisao1 = 4
    if decisao1 == 2:
      print("Você decidiu parar")
      print("O seu baralho vale: ",soma2)
    elif decisao1 == 3:
        print(f"Jogo abandonado por {nome}")
        soma2 = 100

    while decisao1 == 2 and soma1 < 21 and soma2 != 21:
      resultado = random.choice(cartas)
      cartas.remove(resultado)
      if resultado == 'A':
        resultado = 11 if soma1 + 11 <= 21 else 1  
      print("\nA carta retirada pelo dealer vale: ",resultado)
      soma1 = soma1 + resultado
      print("O baralho atual do dealer vale: ",soma1)
      if soma1 < 21 and soma1 > soma2:
        print("O dealer decidiu parar")
        decisao1 = 0
      print("Fim de rodada")
      print("________________________________________________________________")

    if soma1 == 21 or soma2 > 21:
      print(f'\nO dealer venceu! -{valor} coins')
      moedas = moedas - valor
      jogar = 3
    elif soma2 == 21 or soma1 > 21:
      print(f'\n{nome} venceu! +{valor*2} coins')
      moedas = moedas + valor
      jogar = 3
    elif soma1 > soma2:
      print(f'\nO dealer venceu! -{valor} coins')
      moedas = moedas - valor
      jogar = 3
    elif soma2 > soma1:
      print(f'\n{nome} venceu! +{valor*2} coins')
      moedas = moedas + valor
      jogar = 3
      