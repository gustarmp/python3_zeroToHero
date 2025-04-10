"""
Faca uma lista de compras com listas
O usuario deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Nao permita que o programa quebre com
erros de indices inexistentes na lista.
"""
import os

lista = []

while True:
    opcao = (input('Lista de compras: \n1. Adicionar item\n2. Remover item\n3. Visualizar lista atual\n0. Sair da lista\nOpcao: '))
    os.system('clear')

    if opcao == '0':
        print('Saiu da lista de compras!')
        break

    elif opcao == '1':
        item = input('Qual item gostaria de adicionar: ')
        lista.append(item)
        os.system('clear')

    
    elif opcao == '2':
        try:
            print('Cod. Item')
            for i,l in enumerate(lista):
                print(f'{i}. {l}')
            print('-' * 45)
            index = int(input('Qual item gostaria de remover (Cod.): '))
            lista.pop(index)
            os.system('clear')

        except (ValueError, IndexError):
            print('Cod. nao encontrado na lista.')
            print('-' * 45)

    elif opcao == '3':
        if lista == []:
            print('Lista vazia.')
            print('-' * 45)
        else:
            print('Cod. Item')
            for i,l in enumerate(lista):
                print(f'{i}. {l}')
            print('-' * 45)
    else:
        print('Opcao invalida, escolha uma opcao valida!')
        print('-' * 45)
