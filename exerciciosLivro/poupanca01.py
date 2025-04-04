# Exercicio 5.11
# Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança. 
# Exiba os valores mês a mês para os 24 primeiros meses. 
# Escreva o total ganho com juros no período.

inicial = float(input('Qual o deposito inicial: R$ '))
juros = float(input('Qual a taxa de juros: ')) / 100
meses = 1
soma = 0

while meses <= 24:
    soma = soma + (inicial * juros)
    inicial = inicial + (inicial * juros)
    print(f'Valor do mes {meses}: R${inicial:.2f}')
    meses = meses + 1
    

print(f'O ganho total com juros foi de: R${soma:.2f}')