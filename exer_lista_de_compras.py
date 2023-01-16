''' Faça uma lista de compras com listas 
O usario deve ter a possibilidade de 
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de indices inexistentes na lista'''

itens = []

while True:

    print('Selecione uma opçao:')
    acao = input('[i]nserir [a]pagar [l]istar [s]air: ').lower()
    if acao.startswith('i'):
        acao_inserir = input ('Digite o item q deseja adicionar: ') 
        itens.append(acao_inserir)
            
    elif acao.startswith('a'):
        for i, item in enumerate(itens):
            print(i, item)
        acao_apagar = input('Digite o indice do item q voce deseja apagar: ')
        try:
            acao_apagar = int(acao_apagar)
            itens.pop(acao_apagar) 
        except: 
            print (' Digite um numero válido')
            continue
    elif acao.startswith('l'):
        for i, item in enumerate(itens):
            print(i, item) 
    elif acao.startswith('s'):
        break         
    else:
        print('acao invalida, tente novamente')
        continue