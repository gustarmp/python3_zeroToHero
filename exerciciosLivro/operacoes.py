# Exercicio 5.22
# Escreva um programa que exiba uma lista de opções (menu): adição, subtração, divisão, multiplicação e sair.
# Imprima a tabuada da operação escolhida.
# Repita até que a opção saída seja escolhida.


while True:
    menu = int(input('Menu - Escolha uma opcao \n1. Adicao\n2. Subtracao\n3. Divisao\n4. Multiplicacao\n0. Sair\nDigite a opcao: '))
    if menu == 0:
        print('Fim do programa.')
        break
    n = int(input('Digite um numero inteiro: '))

    if menu == 1:
        t = 1
        while t <= 10:
            print(f'{n} + {t} = {n + t}')
            t += 1
    if menu == 2:
        t = 1
        while t <= 10:
            print(f'{n} - {t} = {n - t}')
            t += 1
    if menu == 3:
        t = 1
        while t <= 10:
            print(f'{n} / {t} = {n / t:.2f}')
            t += 1
    if menu == 4:
        t = 1
        while t <= 10:
            print(f'{n} * {t} = {n * t}')
            t += 1
    else:
        print('Opcao invalida.')