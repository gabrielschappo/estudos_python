import re

cpf = input('Informe o cpf: ')
lista = []
lista_nums = []
nums = 0
soma = 0

def validar(cpf,lista,nums,lista_nums):
    lista = re.findall(r'\d+', cpf)
    nums = int(''.join(map(str, lista)))
    print(f'cpf informado: {nums}')
    lista_nums = [int(digito) for digito in str(abs(nums))]
    return lista_nums
    
def verificar(nums_cpf, soma):
    a = 0
    for x in range(10,1,-1):
        soma += nums_cpf[a] * x
        a += 1
    soma = soma % 11
    soma = 11 - soma
    if (soma < 10 and soma == nums_cpf[9]) or (soma >= 10 and nums_cpf[9] == 0):
        soma = 0
        a = 0
        for x in range(11,1,-1):
            soma += nums_cpf[a] * x
            a += 1
        soma = soma % 11
        soma = 11 - soma
        if (soma < 10 and soma == nums_cpf[10]) or (soma >= 10 and nums_cpf[10] == 0):
            print('CPF válido(códigos verificadores OK)')
            return 1
        else:
            print('CPF inválido(codigo verificador 2)')
            return 0
    else:
        print('CPF inválido(codigo verificador 1)')
        return 0
    

nums_cpf = validar(cpf,lista,nums,lista_nums)

if len(nums_cpf) == 11 and (nums_cpf[0] != nums_cpf[1] or nums_cpf[0] != nums_cpf[2] or nums_cpf[0] != nums_cpf[3] or nums_cpf[0] != nums_cpf[4] or nums_cpf[5] != nums_cpf[6] or nums_cpf[0] != nums_cpf[7] or nums_cpf[0] != nums_cpf[8] or nums_cpf[0] != nums_cpf[9] or nums_cpf[0] != nums_cpf[10]):
    print('Números = 11')
    valido = verificar(nums_cpf, soma)
else:
    print('CPF inválido(números != 11 ou iguais)')


