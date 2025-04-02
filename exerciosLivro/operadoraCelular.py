# Capitulo 4.1.2

plano = str(input('Qual o seu plano de celular? \n'))

if plano == 'falopouco':
    minutosNoPlano = 100
    extra = 0.20
    valor = 50
if plano == 'falomuito':
    minutosNoPlano = 500
    extra = 0.15
    valor = 99

if plano != 'falomuito' and plano != 'falopouco':
    print('Nao reconhecemos esse plano!')

if plano == 'falopouco' or plano == 'falomuito':
    minutosConsumidos = int(input('Quantos minutos voce consumiu? \n'))
    print('Voce vai pagar: ')
    print(f'Preco do plano: R${valor:.2f}')
    suplemento = 0
    if minutosConsumidos > minutosNoPlano:
        suplemento = extra * (minutosConsumidos - minutosNoPlano)
    print(f'Suplemento: R${suplemento:.2f}')
    print(f'Total a pagar: R${valor + suplemento:.2f}')