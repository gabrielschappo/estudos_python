estoque = []
vendas = []
venda_atual = []
id_venda = 0

def menu():
    print('\nMENU:')
    print('\n1- Registrar venda\n2- Consultar/modificar estoque\n3- Ver vendas')
    escolha = int(input('Digite o número do que deseja realizar: '))
    if escolha == 1:
        registrar_venda()
    elif escolha == 2:
        consultar_estoque()
    elif escolha == 3:
        vizualizar_vendas()
    else:
        print('Opção inválida')
        menu()


def adicionar_produto():
    produto = input('\nInforme o produto que deseja adicionar: ')
    quantidade = int(input('Informe a quantidade: '))
    valor = float(input('Informe o valor: '))
    if quantidade < 0:
        print('Quantidade inválida.')
        menu()
    if all(d['nome'] != produto for d in estoque):
        estoque.append({'nome':produto,'quantidade':quantidade,'preco':valor})
        print('Produto criado no estoque.')
        print(f'{estoque[-1]}')
        menu()
    else:
        print('Produto já presente no estoque.')
        menu()

def remover_produto():
    produto = input('\nInforme o produto que deseja remover: ')
    if all(d['nome'] != produto for d in estoque):
        print(f'{produto} não está presente no estoque.')
        menu()
    else:
        for x in estoque:
            if x['nome'] == produto:
                estoque.remove(estoque[estoque.index(x)])
        print(f'{produto} removido do estoque.')
        menu()
        
def consultar_estoque():
    print('\nEstoque:')
    for x in estoque:
        print(f'\nProduto: {estoque[estoque.index(x)]['nome']}')
        print(f'Quantidade: {estoque[estoque.index(x)]['quantidade']}')
        print(f'Preço: {estoque[estoque.index(x)]['preco']}')
    print('\n0- Voltar ao menu\n1- Modificar produto\n2- Adicionar novo produto\n3- Remover produto existente')
    escolha = int(input('Informe o número do que deseja realizar: '))
    if escolha == 0:
        menu()
    elif escolha == 1:
        produto = input('Informe o produto que deseja modificar: ')
        if all(d['nome'] != produto for d in estoque):
            print(f'{produto} não está presente no estoque.')
            menu()
        for x in estoque:
            if x['nome'] == produto:
                print(f'\nProduto: {estoque[estoque.index(x)]['nome']}')
                print(f'Quantidade: {estoque[estoque.index(x)]['quantidade']}')
                print(f'Preço: {estoque[estoque.index(x)]['preco']}')
        estoque[estoque.index(x)]['nome'] = input('Digite o novo nome do produto: ')
        estoque[estoque.index(x)]['quantidade'] = int(input('Digite a nova quantidade do produto: '))
        estoque[estoque.index(x)]['preco'] = float(input('Digite o novo preço do produto: '))
        print('\nProduto atualizado:')
        print(f'\nProduto: {estoque[estoque.index(x)]['nome']}')
        print(f'Quantidade: {estoque[estoque.index(x)]['quantidade']}')
        print(f'Preço: {estoque[estoque.index(x)]['preco']}')
    elif escolha == 2:
        adicionar_produto()
    elif escolha == 3:
        remover_produto()
    menu()

def registrar_venda():
    global id_venda  
    venda_atual = []  
    valor_venda = 0
    print('\n0- Voltar ao menu\n1- Adicionar produto\n2- Remover produto\n3- Finalizar venda')
    escolha = int(input('Digite o número do que deseja realizar: '))
    while escolha != 3:
        if escolha == 0:
            menu()
        elif escolha == 1:
            produto = input('Informe o produto que deseja adicionar: ')
            quantidade = int(input('Informe a quantidade desse produto: '))
            desconto = float(input('Informe o desconto(1=100%): '))
            if all(d['nome'] != produto for d in estoque):
                print('O produto informado não consta no estoque.')
            else:
                for x in estoque:
                    if x['nome'] == produto:
                        if quantidade > estoque[estoque.index(x)]['quantidade']:
                            print(f'Quantidade maior do que a presente no estoque({estoque[estoque.index(x)]['quantidade']})')
                        elif 0 > desconto > 1:
                            print('Desconto inválido(deve estar entre 0(0%) e 1(100%))')
                        else:
                            valor_item = (estoque[estoque.index(x)]['preco'] * (1-desconto)) * quantidade
                            valor_venda += valor_item
                            venda_atual.append({
                                'produto': produto,
                                'quantidade': quantidade,
                                'desconto': f'{desconto*100}%',
                                'valor': valor_item
                            })
        elif escolha == 2:
            if not venda_atual:
                print('Nenhum produto foi adicionado à venda ainda.')
            else:
                print('\nProdutos na venda:')
                for idx, item in enumerate(venda_atual):
                    print(f"{idx + 1} - Produto: {item['produto']}, Quantidade: {item['quantidade']}, Valor: {item['valor']:.2f}")
                item_remover = int(input('Digite o número do produto que deseja remover (ou 0 para cancelar): '))
                if 0 < item_remover <= len(venda_atual):
                    produto_removido = venda_atual.pop(item_remover - 1)
                    valor_venda -= produto_removido['valor']
                    print(f"Produto {produto_removido['produto']} removido da venda.")
                else:
                    print('Opção inválida.')
        print('\n0- Voltar ao menu\n1- Adicionar produto\n2- Remover produto\n3- Finalizar venda')
        escolha = int(input('Digite o número do que deseja realizar: '))
    
    if escolha == 3:
        print(f'\nItens na venda: {venda_atual}')
        print(f'Valor total: {valor_venda:.2f}')
        valor_cliente = float(input('\nInforme o valor dado pelo cliente: '))
        while valor_cliente < valor_venda:
            print('Valor informado é menor que o valor total da venda.')
            valor_cliente = float(input('Informe o valor dado pelo cliente: '))
        troco = valor_cliente - valor_venda
        print(f'Troco: {troco:.2f}')
        escolha = int(input('Digite 1 para confirmar ou 0 para cancelar: '))
        if escolha == 0:
            registrar_venda()
        else:
            vendas.append({'id': id_venda, 'detalhes': venda_atual, 'valor total': valor_venda})
            print('Venda concluída.')
            print(f'ID da venda: {id_venda}\nDetalhes: {venda_atual}\nValor total: {valor_venda}')
            id_venda += 1  
            for y in estoque:
                for x in venda_atual:
                    if x['produto'] == y['nome']:
                        y['quantidade'] -= x['quantidade']
            menu()

def vizualizar_vendas():
    print('\nVENDAS')
    if vendas == []:
        print('\nNenhuma venda foi realizada.')
    for x in vendas:
        print(f'\nID da Venda: {x['id']}\nDetalhes: {x['detalhes']}\nValor total: {x['valor total']}')
    menu()
        


menu()