"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""
nome = 'Gustavo'
preco = 1000.95897643
variavel = '%s, o preco e R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %i e %04x' % (3002, 3002))