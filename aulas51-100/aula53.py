lista = ['Maria', 'Helena', 'Luiz']
lista.append('Joao')

listaEnumerada = enumerate(lista)

for indice, nome in enumerate(lista): # for i in enumerate(lista):
    print(f'Indice: {indice} Valor: {nome}')
