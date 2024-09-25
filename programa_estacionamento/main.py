import numpy as np
import random

setor_a = np.array(['0000000','0000000','0000000','0000000','0000000'])
setor_b = np.array(['0000000','0000000','0000000','0000000','0000000'])
setor_c = np.array(['0000000','0000000','0000000','0000000','0000000'])
placa = ''

def ocupar_vaga(placa):
    placa = input('\nInforme a placa do veículo: ').upper()
    while placa in (setor_a) or placa in (setor_b) or placa in (setor_c):
        print(f'Veículo com placa {placa} já estacionado.')
        placa = input('Informe a placa do veículo: ')
    while len(placa) != 7:
        print('Placa inválida. Uma placa deve conter sete carácteres.')
        placa = input('Informe a placa do veículo: ')
    escolher_vaga(placa)

def escolher_vaga(placa):
    possiveis = ['a','b','c']
    if '0000000' not in setor_a:
        possiveis.remove('a')
    if '0000000' not in setor_b:
        possiveis.remove('b')
    if '0000000' not in setor_c:
        possiveis.remove('c')
    if possiveis == []:
        print('\nTodas as vagas já foram preenchidas.')
        menu(placa)
    setor = random.choice(possiveis)
    disponiveis = []
    if setor == 'a' and '0000000' in (setor_a):
        for x in range(5):
            if setor_a[x] == '0000000':
                disponiveis.append(x)
        vaga = random.choice(disponiveis)
        setor_a[vaga] = placa
    elif setor == 'b' and '0000000' in (setor_b):
        for x in range(5):
            if setor_b[x] == '0000000':
                disponiveis.append(x)
        vaga = random.choice(disponiveis)
        setor_b[vaga] = placa
    elif setor == 'c' and '0000000' in (setor_c):
        for x in range(5):
            if setor_c[x] == '0000000':
                disponiveis.append(x)
        vaga = random.choice(disponiveis)
        setor_c[vaga] = placa
    print(f'\nVeículo com placa {placa} estacionado na vaga {setor}{vaga}')
    menu(placa)
    
def liberar_vaga(placa):
    setores = [setor_a, setor_b, setor_c]
    for setor_numero, setor in enumerate(setores):
        for i in range(len(setor)):
            if setor[i] == placa:
                setor[i] = '0000000'
                print(f"\nVeículo com placa {placa} removido.")
                menu(placa)
    print(f"\nVeículo com placa {placa} não encontrado em nenhum setor")
    menu(placa)

def exibir_vagas(placa):
    formato_a = lambda x: ', '.join(f'a{i}' for i in x)
    formato_b = lambda x: ', '.join(f'b{i}' for i in x)
    formato_c = lambda x: ', '.join(f'c{i}' for i in x)
    disponiveis_a = []
    disponiveis_b = []
    disponiveis_c = []
    for x in range(5):
        if setor_a[x] == '0000000':
            disponiveis_a.append(x)
        if setor_b[x] == '0000000':
            disponiveis_b.append(x)
        if setor_c[x] == '0000000':
            disponiveis_c.append(x)
    print(f'\nVagas disponíveis no setor A: {formato_a(disponiveis_a)}')
    print(f'Vagas disponíveis no setor B: {formato_b(disponiveis_b)}')
    print(f'Vagas disponíveis no setor C: {formato_c(disponiveis_c)}')
    menu(placa)

def consultar_veiculo(placa):
    formato = lambda x: ', '.join(map(str, x))
    if placa in (setor_a):
        print(f'\nO veículo com placa {placa} está estacionado em a{formato(np.where(setor_a == placa)[0])}')
    elif placa in (setor_b):
        print(f'\nO veículo com placa {placa} está estacionado em b{formato(np.where(setor_b == placa)[0])}')
    elif placa in (setor_c):
        print(f'\nO veículo com placa {placa} está estacionado em c{formato(np.where(setor_c == placa)[0])}')
    else:
        print(f'\nO veículo com placa {placa} não está estacionado no momento.')
    menu(placa)

def menu(placa):
    print('\n')
    escolha = 0
    while escolha not in (1,2,3,4):
        print('1- Ocupar vaga:\n2- Liberar vaga\n3- Exibir vagas\n4- Consultar veículo')
        escolha = int(input('Digite o número do que deseja fazer: '))
    if escolha == 1:
        ocupar_vaga(placa)
    elif escolha == 2:
        placa = input("\nDigite a placa do veículo que deseja remover: ").upper()
        liberar_vaga(placa)
    elif escolha == 3:
        exibir_vagas(placa)
    elif escolha == 4:
        placa = input('\nDigite a placa do veículo que deseja consultar: ').upper()
        consultar_veiculo(placa)


menu(placa)