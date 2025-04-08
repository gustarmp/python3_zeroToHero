"""
Iterando strings com while
"""
#       012345678912345
#nome = 'Gustavo Ricardo'  # Iteráveis
#      1110987654321

nome = input('Digite o seu nome:')
 
tamanho_nome = len(nome) - 1
contador = 0
nova_string = 0
 
while tamanho_nome >= 0: 
   nova_string = print(f'{nome[contador]}', end='*')
   contador += 1
   tamanho_nome -= 1