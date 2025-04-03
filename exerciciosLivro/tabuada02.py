# Exercicio 5.7
# Modifique o programa anterior de forma que o usuário também digite o início e o fim da tabuada, em vez de começar com 1 e 10.

n = int(input('Digite um numero: '))
x = int(input('Qual o inicio da tabuada: '))
tam = int(input('Qual o final da tabuada: '))
while x <= tam:
    print(f'{x} x {n} =', x * n )
    x = x + 1