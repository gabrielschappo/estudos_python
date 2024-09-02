from sys import exit
def gold_room():
  while True:
    print('\nEsse quarto está cheio de ouro. Quanto você pega?')
    choice = input(">")
    if choice.isdigit():
        how_much = int(choice)
        break
    else:
        print("Amigo, aprenda a digitar um número.")


  if how_much < 50:
    print("Boa, você não é ganancioso, você ganhou!")
    recomecar()
  else:
    dead("Seu ganancioso desgraçado!")


def bear_room():
  print("\nTem um urso nesse quarto.")
  print("O urso tem bastante mel.")
  print("O grande urso está na frente de outra porta.")  
  print("Como você vai tirar o urso daí? Pegar o mel ou assustar o urso")


  while True:
    choice = input("> ")
    if choice == "pegar o mel":
     dead("O urso olha para você e te dá uma patada no rosto e te mata.")
    elif choice == "assustar o urso":
      print("O urso se move da porta, com medo.")
      print("Você pode passar agora.")
      gold_room()


    #Mudamos o choice para o usuario poder entrar na porta


    else:
      print("Não tenho ideia do que isso significa.")








def cthulhu_room():
  print("\nAqui você vê o grande demônio Cthulhu.")
  print("O que há que seja essa aberração, encare-o e vá a loucura.")
  print("Você luta pela sua vida ou aceita seu fim e comete suicídio?")
  choice = input("> ")
  #Mudamos esse if para ganhar e ir para o gold room
  if "luta" in choice:
    print("\nDe alguma forma misteriosa, você se transforma em uma máquina de matar")      #BUG ARRUMAR
    print("Conforme a adrenalina corre em seu sangue, você parte pra cima de Cthulhu...")
    print("Vo-Você derrotou ele, você pode passar agora")
    gold_room()
  elif "suicidio" in choice:
    dead("Ótimo, Cthulhu achou você deliciosamente saboroso!")
  else:
    cthulhu_room()






# Nova def caso suba a escada
def darth_vader_room():
  print("\nAo subir a escada você se depara com o Darth Vader.")
  print("O imperador das estrelas se questiona da sua presença.")
  print("O mesmo se posiciona a uns 2 metros da porta")
  print("Ao observar o quarto, há um sabre de luz no chão")
  print("O que você faz? pegar sabre ou correr")
  choice = input("> ")
  if "correr" in choice:
    print("Foi por pouco! Você passou para o próximo quarto")
    gold_room()
  elif "pegar sabre" in choice:
    dead("Putz! Você acha mesmo que ganharia do maior vilão da galáxia? Você está morto.")
  else:
    print("Digite uma das opções descritas")








def dead(why):
  print(why)     #Bom trabalho removido
  print('Fim de jogo.')
  recomecar()


def start():
  print("\nVocê chega em um quarto escuro.")
  print("Tem uma porta à sua ESQUERDA, uma à sua DIREITA, uma ESCADA e uma JANELA quebrada escrito volte com sangue")
  print("Qual você escolhe para abrir?")
  choice = input("> ")
  if choice == "esquerda":
    bear_room()
  elif choice == "direita":
    cthulhu_room()
  elif choice == "janela":
    print("Você fica com medo daquela casa.")
    print("Ao observar a porta principal aberta, você foge do local em segurança")
    recomecar()
  elif choice == "escada":
    print("Você sobe a escada")
    darth_vader_room()
  else:
    dead("Você fica perambulando pelo quarto até morrer de fome.")












#adicionamos uma introdução para o jogo
def pre_start():
  print('Wineland - 1879')
  print('Você é um mero cidadão interessado em crescer na vida.')
  print('A cidade não para de falar sobre uma tal casa misteriosa lotada de riquezas.')
  print('O que poucos sabem, é que nela moram criaturas misteriosas.')
  while True:
    print('Você quer tentar a sorte e ir para essa aventura?(sim ou nao)')
    choice = input('>')
    if choice == 'sim':
      print('Você vai até esse local e abre a porta.')
      start()
    elif choice == 'nao':
      dead('Você viveu a vida como um miserável e morreu de tanto trabalhar.')
    else:
      print('Está indeciso?')


def recomecar():
    while True:
        print('\nDeseja jogar novamente?(S/N)')
        choice = input('>')
        if choice.lower() == 's':
            pre_start()
        elif choice.lower() == 'n':
            exit(0)
        else:
            print('Digite uma resposta válida')




pre_start()
