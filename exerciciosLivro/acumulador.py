# Capitulo 5.2 - Acumuladores
# Nao e um exercicio mas achei interessante o codigo

c = 1
soma = 0

while c <= 10:
    v = int(input(f'Digite o {c} numero: '))
    soma = soma + v
    c = c + 1
print(f'Soma: {soma}')