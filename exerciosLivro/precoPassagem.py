# Exercicio 4.6
# Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$ 0,45 para viagens mais longas.

distancia = float(input('Qual a distancia da viajem? \nkm: '))

if distancia > 200:
    valor = distancia * 0.45
else:
    valor = distancia * 0.50

print(f'Preco da viagem: R${valor:.2f}')