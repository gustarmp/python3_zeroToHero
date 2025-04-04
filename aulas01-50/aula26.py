"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""

variavel = 'ABCD'
print(f'{variavel}')
print(f'{variavel: >10}') # utilizando f-string podemos criar espacos em branco.
print(f'{variavel: <10}') 
print(f'{variavel:*^10}') # tambem podemos especificar o placeholder em vez de espacos por exemplo (*).
print(f'{1000.243242423:.2f}') # casas decimais com 2 digitos depois da virgula.
print(f'{1000.4873648123746:0=+10,.1f}') # .1f para uma casa depois da virgula, 0=+10 forcando o valor a ter 10 caracteres e mostrar um '+' se o valor for positivo, e preenchendo com zeros depois do sinal de '+'.
print(f'O hexadecimal de 1500 é {1500:04x}') 
print(f'{variavel!r}')