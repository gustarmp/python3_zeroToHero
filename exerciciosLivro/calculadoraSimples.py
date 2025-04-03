# Exercicio 4.10
# Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. Você deve poder calcular soma (+), subtração (-), multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada.

a = float(input('Digite o primeiro valor: '))
b = float(input('Digite o segundo valor: '))
operacao = str(input('Qual operacao voce gostaria de fazer?\n 1. soma\n 2. subtracao\n 3. multiplicacao\n 4. divisao\n'))

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