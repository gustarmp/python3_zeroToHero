"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número inteiro, informe que não é um número inteiro.
"""

try:
    num = int(input('Digite um numero para saber se e par ou impar: '))
    if num % 2 == 0:
        print('Esse numero e par!')
    else:
        print('Esse numero e impar!')
except:
    print('Voce nao digitou um numero inteiro.')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = int(input('Qual a hora atual: '))

if hora <= 11:
    print('Bom dia!')
elif hora <= 17:
    print('Boa tarde!')
else:
    print('Boa noite!')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = str(input('Qual o seu nome: '))
tamanhoNome = len(nome)

if tamanhoNome <= 4:
    print('Seu nome e curto!')
elif tamanhoNome in (5,6):
    print('Seu nome e normal!')
else:
    print('Seu nome e muito grande!')
