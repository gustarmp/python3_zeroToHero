# Operadores in e not in
# Strings são iteráveis, pode navegar item por item.
#  0 1 2 3 4 5
#  O t á v i o
# -6-5-4-3-2-1

#nome = 'Gustavo'
# print(nome[2]) # Puxa o valor do indice da string
# print(nome[-2]) # Puxa o valor do indice da string do final pro comeco
#print('a' in nome)
#print('z' in nome)
#print('avo' not in nome)
#print('avo' in nome)

nome = input('Digite o seu nome: ')
encontrar = input('Digite o que gostaria de encontrar: ')

if encontrar in nome:
    print(f'{encontrar} esta em {nome}!')
else:
    print(f'{encontrar} nao esta em {nome}!')