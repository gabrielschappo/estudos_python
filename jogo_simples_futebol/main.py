import random
from random import randint
from tkinter import *

meu_clube = 'Joinville'
nome = input("Digite o nome do seu jogador: ")
print(f'\nNovo jogador contratado pelo {meu_clube}!\n{nome} chega como uma promessa para somar ao elenco!\nO que podemos esperar dele...')
opcoes = "1- Treinamento\n2- Jogar partida"
dinheiro = 10
habilidade = 0
gols_temp = 0
pontos = 0
nota_soma = 0
fase = 1
jogos = 0

adversarios = ['Cricíuma','Avaí','Marcílio Dias','Figueirense','Barra','Brusque','Hercílio Luz','Chapecoense','Concórdia','Inter de Lages','Nação']
rodada = 0
for rodada in range(11):
  meus_gols = 0
  rodada = rodada + 1
  adversario = random.choice(adversarios)
  adversarios.remove(adversario)
  print(f'\n----------------------RODADA {rodada}----------------------\n \n{meu_clube} x {adversario}')

  print(opcoes)
  menu = int(input("O que deseja fazer? "))
  while menu != 1 and menu != 2:
    print(opcoes)
    menu = int(input("Essa opção não existe! O que deseja fazer? "))
  while menu == 1:
    print("\nTREINAMENTO")
    print(f'\nVocê tem {dinheiro:.2f} reais')
    print(f'Seu nível de habilidade é {habilidade}')
    treino = int(input(f'Digite 1 para treinar({(habilidade*10)+10} reais) ou 0 para voltar ao menu: '))
    while treino == 1 and dinheiro < (habilidade * 10) + 10:
      print("Dinheiro insuficiente!")
      treino = 0
    if treino == 0:
      print(opcoes)
      menu = int(input("O que deseja fazer? "))
    elif treino == 1 and dinheiro >= habilidade * 10:
      habilidade += 1
      dinheiro = dinheiro - habilidade * 10
      print(f'Treino concluído! -{habilidade*10} reais')
  if menu == 2:
    print("\nVamos para o jogo!")
    print("Você terá um número de lances durante a partida baseados em sua habilidade! \nTente tomar as decisões que parecem mais corretas!")
    if habilidade == 0:
      njogadas = [0,1,2]
    elif habilidade == 1 or habilidade == 2:
      njogadas = [1,2,3]
    elif habilidade == 3 or habilidade == 4:
      njogadas = [3,4]
    elif habilidade == 5 or habilidade == 6:
      njogadas = [3,4,5]
    elif habilidade == 7 or habilidade == 8:
      njogadas = [5,6]
    elif habilidade == 9:
      njogadas = [5,6,7,8]
    else:
      njogadas = [7,8,9,10]
    jogadas_partida = random.choice(njogadas)
    possiveis = ['passedefesa','passeataque','cruzamento','escanteio','penalti','chutearea','chutefora','cabeceio','faltaperto','faltalonge','contraataque']
    if jogadas_partida == 0:
      print("Você foi substituído sem tocar na bola.")
    nota = 7
    gol_local = 0
    gol_adversario = 0
    for toques in range(jogadas_partida):
      jogada = random.choice(possiveis)
      certo = [1,2,3]
      if jogada == 'passedefesa':
        possiveis.remove('passedefesa')
        print("\nBola recebida na defesa!")
        print("1- passe para o goleiro\n2- passe para o ataque\n3- passe para a defesa")
        decisao = int(input("O que vai fazer? "))
        if habilidade < 3:
          certo = [1,2,3]
        elif habilidade == 4 or habilidade == 5 or habilidade == 3:
          certo = [1,2,3,decisao]
        elif habilidade == 6 or habilidade == 7:
          certo = [1,2,3,decisao,decisao]
        elif habilidade == 8 or habilidade == 9:
          certo = [1,2,3,decisao,decisao,decisao]
        else:
          certo = [1,2,3,decisao,decisao,decisao,decisao]
        certo = random.choice(certo)
        if decisao == certo:
          print(f'Bom passe de {nome}!')
          nota += 0.5
        elif decisao == 1:
          print(f'Passe fraco de {nome} para o goleiro! O jogador do {adversario} recuperou a bola.\n GOL DELES!')
          gol_adversario += 1
          nota -= 2
        elif decisao == 2:
          print(f'Chutão para o ataque! {adversario} recuperou a bola.')
          nota -= 1
        elif decisao == 3:
          print(f'Passe ruim de {nome} para a defesa! {adversario} recuperou a bola.\n GOL DELES!')
          gol_adversario += 1
          nota -= 2

      elif jogada == 'passeataque':
        possiveis.remove('passeataque')
        print("\nBola recebida no ataque!")
        print("1- passe para trás\n2- passe para a lateral\n3- passe para a área")
        decisao = int(input("O que vai fazer? "))
        if habilidade < 3:
          certo = [1,2,3]
        elif habilidade == 4 or habilidade == 5 or habilidade == 3:
          certo = [1,2,3,decisao]
        elif habilidade == 6 or habilidade == 7:
          certo = [1,2,3,decisao,decisao]
        elif habilidade == 8 or habilidade == 9:
          certo = [1,2,3,decisao,decisao,decisao]
        else:
          certo = [1,2,3,decisao,decisao,decisao,decisao]
        certo = random.choice(certo)
        if decisao == certo and decisao == 1:
          print(f'Bom passe de {nome}!')
          nota += 0.5
        elif decisao == certo and decisao == 2:
          print(f'Linda bola enfiada por {nome}!')
          golo = randint(1,3)
          if golo == 1:
            print(f'Cruzamento e gol do {meu_clube}')
            nota += 1
            gol_local += 1
          else:
            nota += 0.5
        elif decisao == certo and decisao == 3:
          print(f'Belo chuveirinho na área feito por {nome}')
          golo = randint(1,3)
          if golo == 1:
            print(f'O toque de cabeça e é gol do {meu_clube}')
            gol_local += 1
            nota += 1.5
          else:
            nota += 0.5           
        elif decisao == 1:
          print(f'Passe fraco para trás! O jogador do {adversario} recuperou a bola e uma falta foi cometida')
          nota -= 1.2
        elif decisao == 2:
          print(f'Passe ruim para a lateral! {adversario} recuperou a bola.')
          nota -= 0.7
        elif decisao == 3:
          print(f'Chuveirinho precipitado de {nome}! {adversario} recuperou a bola.')
          nota -= 0.7

      elif jogada == 'cruzamento':
        print('\nBola recebida na lateral do campo!')
        print('1- Cruzamento na entrada da área\n2- Cruzamento na pequena área\n3- Levar a bola para a linha de fundo')
        decisao = int(input("O que vai fazer? "))
        if habilidade < 3:
          certo = [1,2,3]
        elif habilidade == 4 or habilidade == 5 or habilidade == 3:
          certo = [1,2,3,decisao]
        elif habilidade == 6 or habilidade == 7:
          certo = [1,2,3,decisao,decisao]
        elif habilidade == 8 or habilidade == 9:
          certo = [1,2,3,decisao,decisao,decisao]
        else:
          certo = [1,2,3,decisao,decisao,decisao,decisao]
        certo = random.choice(certo)
        if decisao == certo and decisao == 1:
          print(f'{nome} cruza na entrada da área...')
          golo = randint(1,4)
          if golo == 1:
            print(f'Jogador do {meu_clube} chuta de primeira e é GOL!')
            gol_local += 1
            nota += 1
          else:
            print(f'Mas o {meu_clube} desperdiça!')
            nota += 0.7
        elif decisao == certo and decisao == 2:
          print(f'{nome} cruza pequena área...')
          golo = randint(1,2)
          if golo == 1:
            print(f'Jogador do {meu_clube} cabeceia e é GOL!')
            gol_local += 1
            nota += 1.5
          else:
            print(f'Mas o {meu_clube} desperdiça!')
            nota += 0.7
        elif decisao == certo and decisao == 3:
          print(f'{nome} carrega a bola para a linha de fundo, tira da marcação mas finaliza para fora!')
          nota += 0.5
        elif decisao == 1 and certo != 1:
          print(f'{nome} cruza mal e o {adversario} afasta a bola!')
          nota -= 0.7
        elif decisao == 2 and certo != 2:
          print(f'{nome} pega mal na bola e o cruzamento sai em tiro de meta para o {adversario}')
          nota -= 1
        elif decisao == 3 and certo != 3:
          print(f'{nome} tenta conduzir a bola para a linha de fundo mas o jogador do {adversario} chega para cortar!')
          nota -= 1

      elif jogada == 'escanteio':
        print(f'\nEscanteio para o {meu_clube}!')
        print("\n1- Bater escanteio curto\n2- Cobrar escanteio na área\n3- Ir para a área")
        decisao = int(input("O que vai fazer? "))
        if habilidade < 3:
          certo = [1,2,3]
        elif habilidade == 4 or habilidade == 5 or habilidade == 3:
          certo = [1,2,3,decisao]
        elif habilidade == 6 or habilidade == 7:
          certo = [1,2,3,decisao,decisao]
        elif habilidade == 8 or habilidade == 9:
          certo = [1,2,3,decisao,decisao,decisao]
        else:
          certo = [1,2,3,decisao,decisao,decisao,decisao]
        certo = random.choice(certo)
        if decisao == certo and decisao == 1:
          print(f'{nome} cobra o escanteio curto e o {meu_clube} tenta um ataque!')
          nota += 0.2
        elif decisao == certo and decisao == 2:
          print(f'{nome} cobra o escanteio na área...')
          golo = randint(1,3)
          if golo == 1:
            print(f'O jogador do {meu_clube} cabeceia e é GOL!')
            gol_local += 1
            nota += 1
          else:
            print(f'Mas a zaga do {adversario} afasta!')
            nota += 0.5
        elif decisao == certo and decisao == 3:
          print(f'O {meu_clube} cobra o escanteio na área...')
          if habilidade > 4:
            golo = randint(1,2)
          else:
            golo = randint(1,3)
          if golo == 1:
            print(f'{nome} cabeceia e é GOL!')
            gol_local += 1
            meus_gols += 1
            nota += 1.5
          else:
            print(f'Mas {nome} cabeceia para fora!')
            nota += 0.5
        elif decisao == 1 and certo != 1:
          print(f'{nome} cobra mal o escanteio e o {adversario} recupera a bola!')
          nota -= 0.9
        elif decisao == 2 and certo != 2:
          print(f'{nome} tenta cobrar o escanteio na área mas erra feio!')
          nota -= 0.7
        elif decisao == 3 and certo != 3:
          print(f'A bola é lançada na área mas {nome} fura e deixa ela passar!')
          nota -= 1

      elif jogada == 'penalti':
        print(f'\nPênalti para o {meu_clube}!')
        print(f'{nome} pega a bola...')
        print("\n1- Buscar o canto\n2- Forte no meio\n3- cavadinha")
        decisao = int(input("O que vai fazer? "))
        if habilidade < 3:
          certo = [1,2,3]
        elif habilidade == 4 or habilidade == 5 or habilidade == 3:
          certo = [1,2,3,decisao]
        elif habilidade == 6 or habilidade == 7:
          certo = [1,2,3,decisao,decisao]
        elif habilidade == 8 or habilidade == 9:
          certo = [1,2,3,decisao,decisao,decisao]
        else:
          certo = [1,2,3,decisao,decisao,decisao,decisao]
        certo = random.choice(certo)
        if decisao == certo and decisao != 3:
          print(f'Ele bate bem e marca para o {meu_clube}')
          meus_gols += 1
          gol_local += 1
          nota += 1
        elif decisao == certo and decisao == 3:
          print(f'BRILHANTE! {nome} converte o pênalti de cavadinha!')
          meus_gols += 1
          gol_local += 1
          nota += 2
        elif decisao != 3 and decisao != certo:
          print(f'Mas desperdiça o pênalti do {meu_clube}')
          nota -= 1.5
        elif decisao == 3 and decisao != certo:
          print(f'BIZARRO! {nome} tenta uma cavadinha mas desperdiça o pênalti!')
          nota -= 2.5

      elif jogada == 'chutearea':
        print(f'\n{nome} recebe a bola na área...')
        print("\n1- Chutar de primeira\n2- Driblar o zagueiro e chutar\n3- Tocar para o lado")
        decisao = int(input("O que vai fazer? "))
        if habilidade < 3:
          certo = [1,2,3]
        elif habilidade == 4 or habilidade == 5 or habilidade == 3:
          certo = [1,2,3,decisao]
        elif habilidade == 6 or habilidade == 7:
          certo = [1,2,3,decisao,decisao]
        elif habilidade == 8 or habilidade == 9:
          certo = [1,2,3,decisao,decisao,decisao]
        else:
          certo = [1,2,3,decisao,decisao,decisao,decisao]
        certo = random.choice(certo)
        if decisao == certo and decisao == 1:
          golo = randint(1,2)
          if golo == 1:
            print("Chuta de primeira e marca!")
            gol_local += 1
            meus_gols += 1
            nota += 1.5
          else:
            print("Chuta de primeira mas o goleiro defende!")
            nota += 0.5
        elif decisao == certo and decisao == 2:
          if habilidade < 5:
            golo = randint(1,3)
          else:
            golo = randint(1,2)
          if golo == 1:
            print(f'Dribla o zagueiro e marca um golaço para o {meu_clube}')
            gol_local += 1
            meus_gols += 1
            nota += 1.5
          else:
            print(f'Dribla o zagueiro mas o goleiro defende!')
            nota += 0.5
        elif decisao == certo and decisao == 3:
          print(f'Toca para o lado e o companheiro afunda a rede! GOL do {meu_clube}')
          gol_local += 1
          nota += 1
        elif decisao == 1 and decisao != certo:
          print(f'Tenta bater de primeira e perde uma grande chance para o {meu_clube}')
          nota -= 1.2
        elif decisao == 2 and decisao != certo:
          print(f'Tenta driblar o zagueiro mas perde a bola!')
          nota -= 1.5
        elif decisao == 3 and decisao != certo:
          print(f'Toca errado e perde uma grande chance para o {meu_clube}')
          nota -= 1.5

      elif jogada == 'chutefora':
        print(f'\n{nome} recebe a bola fora da área...')
        print("\n1- Chutar para o gol\n2- Tocar para trás\n3- Tocar para o lado")
        decisao = int(input("O que vai fazer? "))  
        if habilidade < 3:
          certo = [1,2,3]
        elif habilidade == 4 or habilidade == 5 or habilidade == 3:
          certo = [1,2,3,decisao]
        elif habilidade == 6 or habilidade == 7:
          certo = [1,2,3,decisao,decisao]
        elif habilidade == 8 or habilidade == 9:
          certo = [1,2,3,decisao,decisao,decisao]
        else:
          certo = [1,2,3,decisao,decisao,decisao,decisao]
        certo = random.choice(certo)
        if decisao == certo:
          if decisao == 1:
            if habilidade < 3:
              golo = randint(1,5)
            elif habilidade < 6:
              golo = randint(1,3)
            else:
              golo = randint(1,2)
            if golo == 1:
              print(f'Bate direto pro gol e... MARCA PARA O {meu_clube.upper()}')
              meus_gols += 1
              gol_local += 1
              nota += 2
            else:
              print(f'Bate direto para o gol e... o goleiro defende!')
              nota += 0.5
          elif decisao == 2:
            print("E recua para a zaga.")
            nota += 0.5
          elif decisao == 3:
            print("E toca para o companheiro ao lado.")
            nota += 0.7
        elif decisao != certo:
          if decisao == 1:
            print("Bate direto pro gol... mas isola a bola!")
            nota -= 0.5
          elif decisao == 2:
            golo = randint(1,3)
            if golo == 1:
              print(f'Toca fraco para trás e perde a bola! No contra-ataque gol do {adversario}!')
              nota -= 1.7
              gol_adversario += 1
            else:
              print(f'Toca fraco para trás e perde a bola! No contra-ataque o {adversario} perde o gol!')
              nota -= 1.2
          elif decisao == 3:
            print(f'Tenta tocar para o lado mas perde a bola!')
            nota -= 0.8

      elif jogada == 'cabeceio':
        print(f'\nO {meu_clube} cruza a bola na área...')
        print("\n1- Cabecear pro gol\n2- Dominar de peito")
        decisao = int(input("O que vai fazer? "))
        if habilidade < 3:
          certo = [1,2]
        elif habilidade == 4 or habilidade == 5 or habilidade == 3:
          certo = [1,2,decisao]
        elif habilidade == 6 or habilidade == 7:
          certo = [1,2,decisao,decisao]
        elif habilidade == 8 or habilidade == 9:
          certo = [1,2,decisao,decisao,decisao]
        else:
          certo = [1,2,decisao,decisao,decisao,decisao]
        certo = random.choice(certo)
        if decisao == certo:
          if decisao == 1:
            golo = randint(1,2)
            if golo == 1:
              print(f'{nome} cabeceia e marca para o {meu_clube}')
              gol_local += 1
              meus_gols += 1
              nota += 1
            else:
              print(f'{nome} cabeceia mas o goleiro defende!')
              nota += 0.5
          elif decisao == 2:
            golo = randint(1,3)
            if golo == 1:
              print(f'{nome} domina de peito e marca um golaço de voleio!')
              gol_local += 1
              meus_gols += 1
              nota += 1.5
            else:
              print(f'{nome} domina de peito, bate de voleio mas o goleiro defende!')
              nota += 0.7
        elif decisao != certo:
          if decisao == 1:
            print(f'{nome} tenta cabecear mas erra o gol!')
            nota -= 0.7
          elif decisao == 2:
            print(f'{nome} domina no peito mas perde a bola na hora de bater!')
            nota -= 1

      elif jogada == 'faltaperto':
        print(f'\nFalta perigosa para o {meu_clube}')
        print("\n1- Chutar forte para o gol\n2- Chutar colocado para o gol\n3- Cruzar na área")
        decisao = int(input('O que vai fazer? '))
        if habilidade < 3:
          certo = [1,2]
        elif habilidade == 4 or habilidade == 5 or habilidade == 3:
          certo = [1,2,decisao]
        elif habilidade == 6 or habilidade == 7:
          certo = [1,2,decisao,decisao]
        elif habilidade == 8 or habilidade == 9:
          certo = [1,2,decisao,decisao,decisao]
        else:
          certo = [1,2,decisao,decisao,decisao,decisao]
        certo = random.choice(certo)
        if decisao == certo:
          if decisao == 1:
            if habilidade >= 3:
              print(f'{nome} bate com força e marca! GOLAÇO!')
              nota += 1
              gol_local += 1
              meus_gols += 1
            else:
              print(f'{nome} bate com força e isola a bola!')
              nota += 0.2
          elif decisao == 2:
            golo = randint(1,2)
            if golo == 1:
              print(f'{nome} cobra no ângulo e marca! GOLAÇO!')
              nota += 1
              gol_local += 1
              meus_gols += 1
            else:
              print(f'{nome} cobra no ângulo mas o goleiro faz uma defesaça!')
              nota += 0.5
          elif decisao == 3:
            golo = randint(1,3)
            if golo == 1:
              print(f'{nome} lança a bola na área, o atacante cabeceia e é GOL do {meu_clube}')
              nota += 0.8
              gol_local += 1
            else:
              print(f'{nome} lança a bola na área mas a defesa afasta!')
              nota += 0.4
        if decisao != certo:
          if decisao == 1:
            print(f'{nome} tenta bater com força mas acerta a barreira!')
            nota -= 0.5
          elif decisao == 2:
            print(f'{nome} cobra de chapa mas acerta a barreira!')
            nota -= 0.6
          elif decisao == 3:
            print(f'{nome} tenta cruzar na área mas erra na força!')
            nota -= 0.8

      elif jogada == 'faltalonge':
        possiveis.remove('faltalonge')
        print(f'\nFalta muito longe para o {meu_clube}!')
        print("\n1- Cobrar direto pro gol\n2- Cruzar na área\n3- Tocar para o lado")
        decisao = int(input("O que vai fazer? "))
        if habilidade < 3:
          certo = [1,2]
        elif habilidade == 4 or habilidade == 5 or habilidade == 3:
          certo = [1,2,decisao]
        elif habilidade == 6 or habilidade == 7:
          certo = [1,2,decisao,decisao]
        elif habilidade == 8 or habilidade == 9:
          certo = [1,2,decisao,decisao,decisao]
        else:
          certo = [1,2,decisao,decisao,decisao,decisao]
        certo = random.choice(certo)
        if decisao == certo:
          if decisao == 1:
            golo = randint(1,10)
            if golo == 1:
              print(f'{nome.upper()} BATE DIRETO E MARCA! GOL DO {meu_clube.upper()}!')
              nota += 1.5
              meus_gols += 1
              gol_local += 1
            else:
              print(f'{nome} tenta bater de muito longe e o goleiro defende!')
              nota += 0.5
          elif decisao == 2:
            golo = randint(1,3)
            if golo == 1:
              print(f'{nome} cruza na área e o atacante marca de cabeça!')
              nota += 1
              gol_local += 1
            else:
              print(f'{nome} cruza a bola na área mas o atacante do {meu_clube} perde a chance!')
              nota += 0.5
          elif decisao == 3:
            print(f'{nome} cobra a falta com um passe simples para o lado!')
            nota += 0.3
        elif decisao != certo:
          if decisao == 1:
            print(f'{nome} tenta bater de muito longe e isola a bola!')
            nota -= 0.8
          elif decisao == 2:
            print(f'{nome} cruza na área mas a defesa do {adversario} afasta!')
            nota -= 0.5
          elif decisao == 3:
            print(f'{nome} cobra a falta com um passe ruim e o {adversario} parte em contra-ataque!')
            nota -= 1

      elif jogada == 'contraataque':
        print(f'\n{meu_clube} recupera a bola e {nome} parte em contra-ataque!')
        print("\n1- Voltar a bola para a defesa\n2- Correr pela lateral\n3- Virar o jogo")
        decisao = int(input("O que vai fazer? "))
        if habilidade < 3:
          certo = [1,2]
        elif habilidade == 4 or habilidade == 5 or habilidade == 3:
          certo = [1,2,decisao]
        elif habilidade == 6 or habilidade == 7:
          certo = [1,2,decisao,decisao]
        elif habilidade == 8 or habilidade == 9:
          certo = [1,2,decisao,decisao,decisao]
        else:
          certo = [1,2,decisao,decisao,decisao,decisao]
        certo = random.choice(certo)
        if decisao == certo:
          if decisao == 1:
            print(f'{nome} decide voltar a bola e recomeçar a jogada!')
            nota += 0
          elif decisao == 2:
            print(f'{nome} conduz a bola na lateral do campo e cruza...')
            golo = randint(1,4)
            if golo == 1:
              print(f'GOL DO {meu_clube.upper()}!')
              nota += 1
              gol_local += 1
            else:
              print(f'Mas o {meu_clube} desperdiça a chance!')
              nota += 0.5
          elif decisao == 3:
            print(f'{nome} faz um ótimo lançamento para virar o jogo!')
            nota += 0.5
        elif decisao != certo:
          if decisao == 1:
            print(f'{nome} toca muito fraco para trás e perde a bola!')
            golo = randint(1,3)
            if golo == 1:
              print(f'GOL DO {adversario.upper()}')
              nota -= 1.5
              gol_adversario += 1
            else:
              print(f'Mas o {adversario} perde a chance de marcar!')
              nota -= 0.8
          elif decisao == 2:
            print(f'{nome} tenta conduzir a bola pela lateral mas é desarmado!')
            nota -= 0.5
          elif decisao == 3:
            print(f'{nome} tenta virar o jogo mas erra o lançamento!')
            nota -= 0.7
    gols_temp += meus_gols
    nota_soma += nota
    gol_local += randint(0,3)
    gol_adversario += randint(0,3)
    print(f'FIM DE JOGO\n{meu_clube} {gol_local}x{gol_adversario} {adversario} ')
    if gol_local > gol_adversario:
      pontos += 3
    elif gol_adversario == gol_local:
      pontos += 1
    if nota > 10:
      nota = 10
    meus_gols = 0
    print(f'Nota de {nome}: {nota:.2f}')
    dinheiro += nota*3
    print(f'+{nota*3:.2f} reais')
print(f'\nFIM DA FASE DE GRUPOS!\n{meu_clube} conquistou {pontos} pontos!')
if pontos >= 25:
  print(f'Passando de fase em primeiro lugar!')
  fase = 2
  finais = 'QUARTAS DE FINAL'
elif pontos > 13:
  print(f'Passando de fase!')
  fase = 2
  finais = 'QUARTAS DE FINAL'
elif pontos > 8:
  print(f'Porém não conseguiu passar de fase!')
else:
  print('E está rebaixado!')
jogo = 0
adversarios = ['Cricíuma','Avaí','Marcílio Dias','Figueirense','Barra','Brusque','Hercílio Luz','Chapecoense','Concórdia','Inter de Lages','Nação']
nc1 = random.choice(adversarios)
adversarios.remove(nc1)
nc2 = random.choice(adversarios)
adversarios.remove(nc2)
nc3 = random.choice(adversarios)
adversarios.remove(nc3)
nc4 = random.choice(adversarios)
adversarios.remove(nc4)
adversario = random.choice(adversarios)
agregado_local = 0
agregado_fora = 0
while fase == 2:
  jogo += 1
  print(f'Confronto definido: {meu_clube} x {adversario}')
  meus_gols = 0
  print(opcoes)
  menu = int(input("O que deseja fazer? "))
  while menu != 1 and menu != 2:
    print(opcoes)
    menu = int(input("Essa opção não existe! O que deseja fazer? "))
  while menu == 1:
    print("\nTREINAMENTO")
    print(f'\nVocê tem {dinheiro:.2f} reais')
    print(f'Seu nível de habilidade é {habilidade}')
    treino = int(input(f'Digite 1 para treinar({(habilidade*10)+10} reais) ou 0 para voltar ao menu: '))
    while treino == 1 and dinheiro < (habilidade * 10) + 10:
      print("Dinheiro insuficiente!")
      treino = 0
    if treino == 0:
      print(opcoes)
      menu = int(input("O que deseja fazer? "))
    elif treino == 1 and dinheiro >= habilidade * 10:
      habilidade += 1
      dinheiro = dinheiro - habilidade * 10
      print(f'Treino concluído! -{habilidade*10} reais')
  if menu == 2:
    print("\nVamos para o jogo!")
    print("Você terá um número de lances durante a partida baseados em sua habilidade! \nTente tomar as decisões que parecem mais corretas!")
    print(f'\n----------------------{finais} jogo {jogo}----------------------\n \n{meu_clube} x {adversario}')
    if habilidade == 0:
      njogadas = [0,1,2]
    elif habilidade == 1 or habilidade == 2:
      njogadas = [1,2,3]
    elif habilidade == 3 or habilidade == 4:
      njogadas = [3,4]
    elif habilidade == 5 or habilidade == 6:
      njogadas = [3,4,5]
    elif habilidade == 7 or habilidade == 8:
      njogadas = [5,6]
    elif habilidade == 9:
      njogadas = [5,6,7,8]
    else:
      njogadas = [7,8,9,10]
    jogadas_partida = random.choice(njogadas)
    possiveis = ['passedefesa','passeataque','cruzamento','escanteio','penalti','chutearea','chutefora','cabeceio','faltaperto','faltalonge','contraataque']
    if jogadas_partida == 0:
      print("Você foi substituído sem tocar na bola.")
    nota = 7
    gol_local = 0
    gol_adversario = 0
    for toques in range(jogadas_partida):
      jogada = random.choice(possiveis)
      certo = [1,2,3]
      if jogada == 'passedefesa':
        possiveis.remove('passedefesa')
        print("\nBola recebida na defesa!")
        print("1- passe para o goleiro\n2- passe para o ataque\n3- passe para a defesa")
        decisao = int(input("O que vai fazer? "))
        if habilidade < 3:
          certo = [1,2,3]
        elif habilidade == 4 or habilidade == 5 or habilidade == 3:
          certo = [1,2,3,decisao]
        elif habilidade == 6 or habilidade == 7:
          certo = [1,2,3,decisao,decisao]
        elif habilidade == 8 or habilidade == 9:
          certo = [1,2,3,decisao,decisao,decisao]
        else:
          certo = [1,2,3,decisao,decisao,decisao,decisao]
        certo = random.choice(certo)
        if decisao == certo:
          print(f'Bom passe de {nome}!')
          nota += 0.5
        elif decisao == 1:
          print(f'Passe fraco de {nome} para o goleiro! O jogador do {adversario} recuperou a bola.\n GOL DELES!')
          gol_adversario += 1
          nota -= 2
        elif decisao == 2:
          print(f'Chutão para o ataque! {adversario} recuperou a bola.')
          nota -= 1
        elif decisao == 3:
          print(f'Passe ruim de {nome} para a defesa! {adversario} recuperou a bola.\n GOL DELES!')
          gol_adversario += 1
          nota -= 2

      elif jogada == 'passeataque':
        possiveis.remove('passeataque')
        print("\nBola recebida no ataque!")
        print("1- passe para trás\n2- passe para a lateral\n3- passe para a área")
        decisao = int(input("O que vai fazer? "))
        if habilidade < 3:
          certo = [1,2,3]
        elif habilidade == 4 or habilidade == 5 or habilidade == 3:
          certo = [1,2,3,decisao]
        elif habilidade == 6 or habilidade == 7:
          certo = [1,2,3,decisao,decisao]
        elif habilidade == 8 or habilidade == 9:
          certo = [1,2,3,decisao,decisao,decisao]
        else:
          certo = [1,2,3,decisao,decisao,decisao,decisao]
        certo = random.choice(certo)
        if decisao == certo and decisao == 1:
          print(f'Bom passe de {nome}!')
          nota += 0.5
        elif decisao == certo and decisao == 2:
          print(f'Linda bola enfiada por {nome}!')
          golo = randint(1,3)
          if golo == 1:
            print(f'Cruzamento e gol do {meu_clube}')
            nota += 1
            gol_local += 1
          else:
            nota += 0.5
        elif decisao == certo and decisao == 3:
          print(f'Belo chuveirinho na área feito por {nome}')
          golo = randint(1,3)
          if golo == 1:
            print(f'O toque de cabeça e é gol do {meu_clube}')
            gol_local += 1
            nota += 1.5
          else:
            nota += 0.5           
        elif decisao == 1:
          print(f'Passe fraco para trás! O jogador do {adversario} recuperou a bola e uma falta foi cometida')
          nota -= 1.2
        elif decisao == 2:
          print(f'Passe ruim para a lateral! {adversario} recuperou a bola.')
          nota -= 0.7
        elif decisao == 3:
          print(f'Chuveirinho precipitado de {nome}! {adversario} recuperou a bola.')
          nota -= 0.7

      elif jogada == 'cruzamento':
        print('\nBola recebida na lateral do campo!')
        print('1- Cruzamento na entrada da área\n2- Cruzamento na pequena área\n3- Levar a bola para a linha de fundo')
        decisao = int(input("O que vai fazer? "))
        if habilidade < 3:
          certo = [1,2,3]
        elif habilidade == 4 or habilidade == 5 or habilidade == 3:
          certo = [1,2,3,decisao]
        elif habilidade == 6 or habilidade == 7:
          certo = [1,2,3,decisao,decisao]
        elif habilidade == 8 or habilidade == 9:
          certo = [1,2,3,decisao,decisao,decisao]
        else:
          certo = [1,2,3,decisao,decisao,decisao,decisao]
        certo = random.choice(certo)
        if decisao == certo and decisao == 1:
          print(f'{nome} cruza na entrada da área...')
          golo = randint(1,4)
          if golo == 1:
            print(f'Jogador do {meu_clube} chuta de primeira e é GOL!')
            gol_local += 1
            nota += 1
          else:
            print(f'Mas o {meu_clube} desperdiça!')
            nota += 0.7
        elif decisao == certo and decisao == 2:
          print(f'{nome} cruza pequena área...')
          golo = randint(1,2)
          if golo == 1:
            print(f'Jogador do {meu_clube} cabeceia e é GOL!')
            gol_local += 1
            nota += 1.5
          else:
            print(f'Mas o {meu_clube} desperdiça!')
            nota += 0.7
        elif decisao == certo and decisao == 3:
          print(f'{nome} carrega a bola para a linha de fundo, tira da marcação mas finaliza para fora!')
          nota += 0.5
        elif decisao == 1 and certo != 1:
          print(f'{nome} cruza mal e o {adversario} afasta a bola!')
          nota -= 0.7
        elif decisao == 2 and certo != 2:
          print(f'{nome} pega mal na bola e o cruzamento sai em tiro de meta para o {adversario}')
          nota -= 1
        elif decisao == 3 and certo != 3:
          print(f'{nome} tenta conduzir a bola para a linha de fundo mas o jogador do {adversario} chega para cortar!')
          nota -= 1

      elif jogada == 'escanteio':
        print(f'\nEscanteio para o {meu_clube}!')
        print("\n1- Bater escanteio curto\n2- Cobrar escanteio na área\n3- Ir para a área")
        decisao = int(input("O que vai fazer? "))
        if habilidade < 3:
          certo = [1,2,3]
        elif habilidade == 4 or habilidade == 5 or habilidade == 3:
          certo = [1,2,3,decisao]
        elif habilidade == 6 or habilidade == 7:
          certo = [1,2,3,decisao,decisao]
        elif habilidade == 8 or habilidade == 9:
          certo = [1,2,3,decisao,decisao,decisao]
        else:
          certo = [1,2,3,decisao,decisao,decisao,decisao]
        certo = random.choice(certo)
        if decisao == certo and decisao == 1:
          print(f'{nome} cobra o escanteio curto e o {meu_clube} tenta um ataque!')
          nota += 0.2
        elif decisao == certo and decisao == 2:
          print(f'{nome} cobra o escanteio na área...')
          golo = randint(1,3)
          if golo == 1:
            print(f'O jogador do {meu_clube} cabeceia e é GOL!')
            gol_local += 1
            nota += 1
          else:
            print(f'Mas a zaga do {adversario} afasta!')
            nota += 0.5
        elif decisao == certo and decisao == 3:
          print(f'O {meu_clube} cobra o escanteio na área...')
          if habilidade > 4:
            golo = randint(1,2)
          else:
            golo = randint(1,3)
          if golo == 1:
            print(f'{nome} cabeceia e é GOL!')
            gol_local += 1
            meus_gols += 1
            nota += 1.5
          else:
            print(f'Mas {nome} cabeceia para fora!')
            nota += 0.5
        elif decisao == 1 and certo != 1:
          print(f'{nome} cobra mal o escanteio e o {adversario} recupera a bola!')
          nota -= 0.9
        elif decisao == 2 and certo != 2:
          print(f'{nome} tenta cobrar o escanteio na área mas erra feio!')
          nota -= 0.7
        elif decisao == 3 and certo != 3:
          print(f'A bola é lançada na área mas {nome} fura e deixa ela passar!')
          nota -= 1

      elif jogada == 'penalti':
        print(f'\nPênalti para o {meu_clube}!')
        print(f'{nome} pega a bola...')
        print("\n1- Buscar o canto\n2- Forte no meio\n3- cavadinha")
        decisao = int(input("O que vai fazer? "))
        if habilidade < 3:
          certo = [1,2,3]
        elif habilidade == 4 or habilidade == 5 or habilidade == 3:
          certo = [1,2,3,decisao]
        elif habilidade == 6 or habilidade == 7:
          certo = [1,2,3,decisao,decisao]
        elif habilidade == 8 or habilidade == 9:
          certo = [1,2,3,decisao,decisao,decisao]
        else:
          certo = [1,2,3,decisao,decisao,decisao,decisao]
        certo = random.choice(certo)
        if decisao == certo and decisao != 3:
          print(f'Ele bate bem e marca para o {meu_clube}')
          meus_gols += 1
          gol_local += 1
          nota += 1
        elif decisao == certo and decisao == 3:
          print(f'BRILHANTE! {nome} converte o pênalti de cavadinha!')
          meus_gols += 1
          gol_local += 1
          nota += 2
        elif decisao != 3 and decisao != certo:
          print(f'Mas desperdiça o pênalti do {meu_clube}')
          nota -= 1.5
        elif decisao == 3 and decisao != certo:
          print(f'BIZARRO! {nome} tenta uma cavadinha mas desperdiça o pênalti!')
          nota -= 2.5

      elif jogada == 'chutearea':
        print(f'\n{nome} recebe a bola na área...')
        print("\n1- Chutar de primeira\n2- Driblar o zagueiro e chutar\n3- Tocar para o lado")
        decisao = int(input("O que vai fazer? "))
        if habilidade < 3:
          certo = [1,2,3]
        elif habilidade == 4 or habilidade == 5 or habilidade == 3:
          certo = [1,2,3,decisao]
        elif habilidade == 6 or habilidade == 7:
          certo = [1,2,3,decisao,decisao]
        elif habilidade == 8 or habilidade == 9:
          certo = [1,2,3,decisao,decisao,decisao]
        else:
          certo = [1,2,3,decisao,decisao,decisao,decisao]
        certo = random.choice(certo)
        if decisao == certo and decisao == 1:
          golo = randint(1,2)
          if golo == 1:
            print("Chuta de primeira e marca!")
            gol_local += 1
            meus_gols += 1
            nota += 1.5
          else:
            print("Chuta de primeira mas o goleiro defende!")
            nota += 0.5
        elif decisao == certo and decisao == 2:
          if habilidade < 5:
            golo = randint(1,3)
          else:
            golo = randint(1,2)
          if golo == 1:
            print(f'Dribla o zagueiro e marca um golaço para o {meu_clube}')
            gol_local += 1
            meus_gols += 1
            nota += 1.5
          else:
            print(f'Dribla o zagueiro mas o goleiro defende!')
            nota += 0.5
        elif decisao == certo and decisao == 3:
          print(f'Toca para o lado e o companheiro afunda a rede! GOL do {meu_clube}')
          gol_local += 1
          nota += 1
        elif decisao == 1 and decisao != certo:
          print(f'Tenta bater de primeira e perde uma grande chance para o {meu_clube}')
          nota -= 1.2
        elif decisao == 2 and decisao != certo:
          print(f'Tenta driblar o zagueiro mas perde a bola!')
          nota -= 1.5
        elif decisao == 3 and decisao != certo:
          print(f'Toca errado e perde uma grande chance para o {meu_clube}')
          nota -= 1.5

      elif jogada == 'chutefora':
        print(f'\n{nome} recebe a bola fora da área...')
        print("\n1- Chutar para o gol\n2- Tocar para trás\n3- Tocar para o lado")
        decisao = int(input("O que vai fazer? "))  
        if habilidade < 3:
          certo = [1,2,3]
        elif habilidade == 4 or habilidade == 5 or habilidade == 3:
          certo = [1,2,3,decisao]
        elif habilidade == 6 or habilidade == 7:
          certo = [1,2,3,decisao,decisao]
        elif habilidade == 8 or habilidade == 9:
          certo = [1,2,3,decisao,decisao,decisao]
        else:
          certo = [1,2,3,decisao,decisao,decisao,decisao]
        certo = random.choice(certo)
        if decisao == certo:
          if decisao == 1:
            if habilidade < 3:
              golo = randint(1,5)
            elif habilidade < 6:
              golo = randint(1,3)
            else:
              golo = randint(1,2)
            if golo == 1:
              print(f'Bate direto pro gol e... MARCA PARA O {meu_clube.upper()}')
              meus_gols += 1
              gol_local += 1
              nota += 2
            else:
              print(f'Bate direto para o gol e... o goleiro defende!')
              nota += 0.5
          elif decisao == 2:
            print("E recua para a zaga.")
            nota += 0.5
          elif decisao == 3:
            print("E toca para o companheiro ao lado.")
            nota += 0.7
        elif decisao != certo:
          if decisao == 1:
            print("Bate direto pro gol... mas isola a bola!")
            nota -= 0.5
          elif decisao == 2:
            golo = randint(1,3)
            if golo == 1:
              print(f'Toca fraco para trás e perde a bola! No contra-ataque gol do {adversario}!')
              nota -= 1.7
              gol_adversario += 1
            else:
              print(f'Toca fraco para trás e perde a bola! No contra-ataque o {adversario} perde o gol!')
              nota -= 1.2
          elif decisao == 3:
            print(f'Tenta tocar para o lado mas perde a bola!')
            nota -= 0.8

      elif jogada == 'cabeceio':
        print(f'\nO {meu_clube} cruza a bola na área...')
        print("\n1- Cabecear pro gol\n2- Dominar de peito")
        decisao = int(input("O que vai fazer? "))
        if habilidade < 3:
          certo = [1,2]
        elif habilidade == 4 or habilidade == 5 or habilidade == 3:
          certo = [1,2,decisao]
        elif habilidade == 6 or habilidade == 7:
          certo = [1,2,decisao,decisao]
        elif habilidade == 8 or habilidade == 9:
          certo = [1,2,decisao,decisao,decisao]
        else:
          certo = [1,2,decisao,decisao,decisao,decisao]
        certo = random.choice(certo)
        if decisao == certo:
          if decisao == 1:
            golo = randint(1,2)
            if golo == 1:
              print(f'{nome} cabeceia e marca para o {meu_clube}')
              gol_local += 1
              meus_gols += 1
              nota += 1
            else:
              print(f'{nome} cabeceia mas o goleiro defende!')
              nota += 0.5
          elif decisao == 2:
            golo = randint(1,3)
            if golo == 1:
              print(f'{nome} domina de peito e marca um golaço de voleio!')
              gol_local += 1
              meus_gols += 1
              nota += 1.5
            else:
              print(f'{nome} domina de peito, bate de voleio mas o goleiro defende!')
              nota += 0.7
        elif decisao != certo:
          if decisao == 1:
            print(f'{nome} tenta cabecear mas erra o gol!')
            nota -= 0.7
          elif decisao == 2:
            print(f'{nome} domina no peito mas perde a bola na hora de bater!')
            nota -= 1

      elif jogada == 'faltaperto':
        print(f'\nFalta perigosa para o {meu_clube}')
        print("\n1- Chutar forte para o gol\n2- Chutar colocado para o gol\n3- Cruzar na área")
        decisao = int(input('O que vai fazer? '))
        if habilidade < 3:
          certo = [1,2]
        elif habilidade == 4 or habilidade == 5 or habilidade == 3:
          certo = [1,2,decisao]
        elif habilidade == 6 or habilidade == 7:
          certo = [1,2,decisao,decisao]
        elif habilidade == 8 or habilidade == 9:
          certo = [1,2,decisao,decisao,decisao]
        else:
          certo = [1,2,decisao,decisao,decisao,decisao]
        certo = random.choice(certo)
        if decisao == certo:
          if decisao == 1:
            if habilidade >= 3:
              print(f'{nome} bate com força e marca! GOLAÇO!')
              nota += 1
              gol_local += 1
              meus_gols += 1
            else:
              print(f'{nome} bate com força e isola a bola!')
              nota += 0.2
          elif decisao == 2:
            golo = randint(1,2)
            if golo == 1:
              print(f'{nome} cobra no ângulo e marca! GOLAÇO!')
              nota += 1
              gol_local += 1
              meus_gols += 1
            else:
              print(f'{nome} cobra no ângulo mas o goleiro faz uma defesaça!')
              nota += 0.5
          elif decisao == 3:
            golo = randint(1,3)
            if golo == 1:
              print(f'{nome} lança a bola na área, o atacante cabeceia e é GOL do {meu_clube}')
              nota += 0.8
              gol_local += 1
            else:
              print(f'{nome} lança a bola na área mas a defesa afasta!')
              nota += 0.4
        if decisao != certo:
          if decisao == 1:
            print(f'{nome} tenta bater com força mas acerta a barreira!')
            nota -= 0.5
          elif decisao == 2:
            print(f'{nome} cobra de chapa mas acerta a barreira!')
            nota -= 0.6
          elif decisao == 3:
            print(f'{nome} tenta cruzar na área mas erra na força!')
            nota -= 0.8

      elif jogada == 'faltalonge':
        possiveis.remove('faltalonge')
        print(f'\nFalta muito longe para o {meu_clube}!')
        print("\n1- Cobrar direto pro gol\n2- Cruzar na área\n3- Tocar para o lado")
        decisao = int(input("O que vai fazer? "))
        if habilidade < 3:
          certo = [1,2]
        elif habilidade == 4 or habilidade == 5 or habilidade == 3:
          certo = [1,2,decisao]
        elif habilidade == 6 or habilidade == 7:
          certo = [1,2,decisao,decisao]
        elif habilidade == 8 or habilidade == 9:
          certo = [1,2,decisao,decisao,decisao]
        else:
          certo = [1,2,decisao,decisao,decisao,decisao]
        certo = random.choice(certo)
        if decisao == certo:
          if decisao == 1:
            golo = randint(1,10)
            if golo == 1:
              print(f'{nome.upper()} BATE DIRETO E MARCA! GOL DO {meu_clube.upper()}!')
              nota += 1.5
              meus_gols += 1
              gol_local += 1
            else:
              print(f'{nome} tenta bater de muito longe e o goleiro defende!')
              nota += 0.5
          elif decisao == 2:
            golo = randint(1,3)
            if golo == 1:
              print(f'{nome} cruza na área e o atacante marca de cabeça!')
              nota += 1
              gol_local += 1
            else:
              print(f'{nome} cruza a bola na área mas o atacante do {meu_clube} perde a chance!')
              nota += 0.5
          elif decisao == 3:
            print(f'{nome} cobra a falta com um passe simples para o lado!')
            nota += 0.3
        elif decisao != certo:
          if decisao == 1:
            print(f'{nome} tenta bater de muito longe e isola a bola!')
            nota -= 0.8
          elif decisao == 2:
            print(f'{nome} cruza na área mas a defesa do {adversario} afasta!')
            nota -= 0.5
          elif decisao == 3:
            print(f'{nome} cobra a falta com um passe ruim e o {adversario} parte em contra-ataque!')
            nota -= 1

      elif jogada == 'contraataque':
        print(f'\n{meu_clube} recupera a bola e {nome} parte em contra-ataque!')
        print("\n1- Voltar a bola para a defesa\n2- Correr pela lateral\n3- Virar o jogo")
        decisao = int(input("O que vai fazer? "))
        if habilidade < 3:
          certo = [1,2]
        elif habilidade == 4 or habilidade == 5 or habilidade == 3:
          certo = [1,2,decisao]
        elif habilidade == 6 or habilidade == 7:
          certo = [1,2,decisao,decisao]
        elif habilidade == 8 or habilidade == 9:
          certo = [1,2,decisao,decisao,decisao]
        else:
          certo = [1,2,decisao,decisao,decisao,decisao]
        certo = random.choice(certo)
        if decisao == certo:
          if decisao == 1:
            print(f'{nome} decide voltar a bola e recomeçar a jogada!')
            nota += 0
          elif decisao == 2:
            print(f'{nome} conduz a bola na lateral do campo e cruza...')
            golo = randint(1,4)
            if golo == 1:
              print(f'GOL DO {meu_clube.upper()}!')
              nota += 1
              gol_local += 1
            else:
              print(f'Mas o {meu_clube} desperdiça a chance!')
              nota += 0.5
          elif decisao == 3:
            print(f'{nome} faz um ótimo lançamento para virar o jogo!')
            nota += 0.5
        elif decisao != certo:
          if decisao == 1:
            print(f'{nome} toca muito fraco para trás e perde a bola!')
            golo = randint(1,3)
            if golo == 1:
              print(f'GOL DO {adversario.upper()}')
              nota -= 1.5
              gol_adversario += 1
            else:
              print(f'Mas o {adversario} perde a chance de marcar!')
              nota -= 0.8
          elif decisao == 2:
            print(f'{nome} tenta conduzir a bola pela lateral mas é desarmado!')
            nota -= 0.5
          elif decisao == 3:
            print(f'{nome} tenta virar o jogo mas erra o lançamento!')
            nota -= 0.7
    gols_temp += meus_gols
    nota_soma += nota
    gol_local += randint(0,3)
    gol_adversario += randint(0,3)
    agregado_local += gol_local
    agregado_fora += gol_adversario
    print(f'FIM DE JOGO\n{meu_clube} {gol_local}x{gol_adversario} {adversario} ')
    if jogo == 2:
      jogos += 2
      print(f'\nPlacar agregado: {meu_clube} {agregado_local}x{agregado_fora} {adversario}')
      if agregado_local > agregado_fora and finais == 'QUARTAS DE FINAL':
        fase = 2
        finais = 'SEMI-FINAL'
        adversarios.remove(adversario)
        adversario = random.choice(adversarios)
        print(f'{meu_clube} vence e está classificado para a semi-final!')
      elif agregado_local > agregado_fora and finais == 'SEMI-FINAL':
        fase = 2
        finais = 'FINAL'
        adversarios.remove(adversario)
        adversario = random.choice(adversarios)
        print(f'{meu_clube} vence e está classificado para a grande final!')
      elif agregado_local > agregado_fora and finais == 'FINAL':
        print(f'\nO {meu_clube.upper()} É CAMPEÃO DO CAMPEONATO CATARINENSE!')
        fase = 0
      elif agregado_fora == agregado_local:
        print('Jogo empatado! Vamos para os pênaltis!')
        print(f'\n{nome} vai para a cobrança!')
        print("\n1- Esquerda\n2- Direita\n3- Meio")
        golo = randint(0,1)
        if golo == 1:
          print(f'{nome} faz o seu!')
        else:
          print(f'{nome} perde sua penalidade')
        pen = [1,2,3,4,5]
        pen_local = random.choice(pen) + golo
        pen.remove(pen_local)
        pen_adversario = random.choice(pen)
        print(f'{meu_clube} {pen_local}x{pen_adversario} {adversario}')
        if pen_local > pen_adversario and finais == 'QUARTAS DE FINAL':
          finais = 'SEMI-FINAL'
          adversarios.remove(adversario)
          adversario = random.choice(adversarios)
          print(f'{meu_clube} classificado para a semi-final nos pênaltis!')
        elif pen_local > pen_adversario and finais == 'SEMI-FINAL':
          finais = 'FINAL'
          adversarios.remove(adversario)
          adversario = random.choice(adversarios)
          print(f'{meu_clube} está classificado para a grande final!')
        elif pen_local > pen_adversario and finais == 'FINAL':
          print(f'\nO {meu_clube.upper()} É CAMPEÃO DO CAMPEONATO CATARINENSE!')
          fase = 0
        else:
          print(f'O {meu_clube} foi eliminado para o {adversario} nos pênaltis.')
          fase = 0
      elif agregado_fora > agregado_local:
        print(f'{meu_clube} foi eliminado para o {adversario} na {finais}')
        fase = 0
      jogo = 0
      agregado_local = 0
      agregado_fora = 0
    if nota > 10:
      nota = 10
    meus_gols = 0
    print(f'Nota de {nome}: {nota:.2f}')
    dinheiro += nota*3
    print(f'+{nota*3:.2f} reais')
    
nota_media = nota_soma / (11 + jogos)
print(f'\n{nome} terminou a temporada com {habilidade} de habilidade.')
print(f'{nome} fez {gols_temp} gols na temporada.')
print(f'{nome} teve uma nota média de {nota_media:.2f} na temporada.')
