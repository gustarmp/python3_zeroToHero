# Exercicio 4.12
# Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para comércios. Calcule o preço a pagar de acordo com a tabela a seguir.

# +---------------------------------------+
# |   Preço por tipo e faixa de consumo   |
# +---------------------------------------+
# | Tipo        | Faixa (kWh)   | Preço   |
# +=======================================+
# | Residencial | Até 500       | R$ 0,40 |
# |             | Acima de 500  | R$ 0,65 |
# +---------------------------------------+
# | Comercial   | Até 1000      | R$ 0,55 |
# |             | Acima de 1000 | R$ 0,60 |
# +---------------------------------------+
# | Industrial  | Até 5000      | R$ 0,55 |
# |             | Acima de 5000 | R$ 0,60 |
# +---------------------------------------+

consumo = float(input('Digite o seu consumo de energia: '))
instalacao = str(input('Digite o seu tipo de instalacao: ')).strip().upper()

if instalacao == 'R':
    kh500ate = 0.40
    kh500acima = 0.65
    if consumo <= 500:
        preco = consumo * kh500ate
    else:
        preco = consumo * kh500acima

elif instalacao == 'C':
    kh1000ate = 0.55
    kh1000acima = 0.60
    if consumo <= 1000:
        preco = consumo * kh1000ate
    else:
        preco = consumo * kh1000acima

elif instalacao == 'I':
    kh5000ate = 0.55
    kh5000acima = 0.60
    if consumo <=5000:
        preco = consumo * kh5000ate
    else:
        preco = consumo * kh5000acima
else:
    print('Entrada de tipo de instalacao invalida!')
    preco = 0

print(f'O preco a se pagar e de R${preco:.2f}')