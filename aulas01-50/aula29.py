"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
numero = input('Dobrar numero: ')

try:
    numero = float(numero)
    print(f'O dobro de {numero} e {numero * 2:.2f}')
except:
    print('Isso nao e um numero!')

#if numero.isdigit():
#    numero = float(numero)
#    print(f'O dobro de {numero} e {numero * 2:.2f}')
#else:
#    print('Isso nao e um numero!')