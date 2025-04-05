# Calculadora com while

while True:
    a = float(input('Digite o primeiro valor: '))
    b = float(input('Digite o segundo valor: '))
    operacao = str(input('Qual operacao voce gostaria de fazer?\n1. soma\n2. subtracao\n3. multiplicacao\n4. divisao\n0. sair\n'))
    if operacao == '0':
        print('Fim do programa.')
        break
    if operacao == '1':
        resultado = a + b
    elif operacao == '2':
        resultado = a - b
    elif operacao == '3':
        resultado = a * b
    elif operacao == '4':
        if b != 0:
            resultado = a / b
        else:
            resultado = 'Erro! Divisao por zero nao e permitida.'
    else:
        resultado = 'Erro! Operacao desconhecida, insira opcao valida.'

    print(f'Resultado da operacao: {resultado}')
    print('*' * 50)
    continue