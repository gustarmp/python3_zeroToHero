"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = str(input('Digite seu nome: '))
idade = input('Digite sua idade: ')
espacoNome = ' ' in nome

if nome and idade:
    print(f'Seu nome e {nome}.')
    print(f'Seu nome invertido e {nome[::-1]}.')
    if espacoNome is True:
        print('Seu nome contem espacos.')
    else:
        print('Seu nome nao contem espacos.')
    print(f'Seu nome contem {len(nome)} letras.')
    print(f'A primeira letra do seu nome e {nome[0]}')
    print(f'A ultima letra do seu nome e {nome[-1]}')
else:
    print('Desculpe, voce deixou campos vazios.')