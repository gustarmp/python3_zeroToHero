"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

def soma(x, y, z):
    print(f'{x=} y={y} {z=}', '|', 'x + y + z = ', x + y + z) # facil para visualizar quando o codigo e executado.

soma(5, 4, 2)