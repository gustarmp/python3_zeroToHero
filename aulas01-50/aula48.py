"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

# string = 'ABCDE'
# lista = ['Joao', 'Maria', 'Fernando', 'Gustavo']
# listaMista = [123, True, 'Gustavo Ricardo', 1.23] # suporta diversos valores de dados.
# lista[0] = 'Luiz' # atualiza o valor de Joao para Luiz, listas sao mutaveis.
# listaVazia = [] # retornar um valor falsy.
# print(lista[0])

# lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2] # usado para deletar o valor 300 da lista.
# numero = lista[2]
# print(lista)
# print(numero)
# lista.append(50) # usado para criar um valor ao final da lista.
# lista.pop(3) # remove o ultimo item da lista, nesse caso o 50.
# lista.append(60)
# lista.append(70)
# lista.insert(1, 11) # primeiro parametro e o indice e o segundo o valor que vai entrar.

# listaA = [1, 2, 3]
# listaB = [4, 5, 6]
# listaC = listaA + listaB
# listaD = listaA.extend(listaB) # .extend nao retorna nada, ele altera diretamente a lista A nesse caso.
# print(listaA)
# print(listaC)

"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

listaA = ['Gustavo', 'Maria']
listaB = listaA.copy()

listaA[0] = 'Joao'
print(listaA)
print(listaB)