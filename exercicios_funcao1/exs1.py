#1
#def calc_maior(a,b,c):
#    if a > b and a > c:
#        return a
#    elif b > a and b > c:
#        return b
#    elif c > a and c > b:
#        return c
#    elif a == b and a == c:
#        return a
#    elif a == b and a > c:
#        return a
#    elif b > a and b == c:
#        return b
#    elif c > b and a == c:
#        return a          
#a = int(input('Informe o primeiro número: '))
#b = int(input('Informe o segundo número: '))
#c = int(input('Informe o terceiro número: '))
#maior = calc_maior(a,b,c)
#print(f'O maior número é igual a: {maior}')

#2
#def perimetro(a,b,c):
#    return a + b + c

#a = int(input('Informe o primeiro lado: '))
#b = int(input('Informe o segundo lado: '))
#c = int(input('Informe o terceiro lado: '))
#if a+b > c or a+c > b or b+c > a:
#    res = perimetro(a,b,c)
#else:
#    res = 'Esses lados não formam um triângulo'
#print(f'O perímetro é igual a: {res}')

#3
#def calculo(nota):
#    if 10 >= nota >= 9:
#        return 'A'
#    elif 8 <= nota < 9:
#        return 'B'
#    elif 7 <= nota < 8:
#        return 'C'
#    elif 6 <= nota < 7:
#        return 'D'
#    elif 6 > nota:
#        return 'F'

#nota = float(input('Informe a nota: '))
#conceito = calculo(nota)
#print(f'O conceito da nota {nota:.2f} é {conceito}')

#4
#aprovacao = 0
#presenca = 1
#def verificar(nota,aulas,faltas,presenca):
#    presenca = aulas / faltas
#    if presenca >= 0.25 and nota >= 6:
#        return 1
#    else:
#        return 0

#nota = float(input('Informe a nota: '))
#aulas = int(input('Informe a quantidade de aulas: '))
#faltas = int(input('Informe a quantidade de faltas: '))
#aprovacao = verificar(nota,aulas,faltas,presenca)
#if aprovacao == 1:
#    print('Aluno aprovado')
#elif aprovacao == 0:
#    print('Aluno reprovado')    

#5
#def verificar(idade):
#    if idade < 16:
#        return 'Não eleitor'
#    elif 16 <= idade < 18 or idade > 65:
#        return 'Eleitor facultativo'
#    else:
#        return 'Eleitor obrigatório'

#idade = int(input('Informe a idade da pessoa: '))
#classe = verificar(idade)
#print(f'A classe do eleitor é: {classe}'

#6
#def verificar(num):
#    if num % 2 == 0:
#        return 1
#    else:
#        return -1

#num = int(input('Informe um número: '))
#par_impar = verificar(num)
#if par_impar == 1:
#    print(f'{num} é par')
#else:
#    print(f'{num} é ímpar')

#7
res = 1
def calcular(num,res):
    if num < 0:
        print('Não existe fatorial de número negativo')
        return 'NONE'
    else:
        for x in range(num):
            res += x * res
        return res
num = int(input('Informe um número: '))
fatorial = calcular(num,res)
print(f'O fatorial de {num} é {fatorial}')
                    