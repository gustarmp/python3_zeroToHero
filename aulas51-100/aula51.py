"""
Introdução ao empacotamento e desempacotamento
"""

nomes = ['Maria', 'Helena', 'Luiz']
nome1, nome2, nome3 = nomes # usado para colocar valores de uma lista em variaveis.
print(nome3)

nomeL, *_ = ['Cleber', 'Geraldo', 'Anna'] # convesao usar o _ para variaveis que nao serao utilizadas, no exemplo Geraldo e Anna serao desconsiderados
print(nomeL)
print(_) 