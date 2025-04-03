# Exercicio 5.6
# Altere o programa anterior para exibir os resultados no mesmo formato de uma tabuada: 2x1 = 2, 2x2 = 4, …

n = int(input('Digite um numero: '))
x = 1
while x <= 10:
    print(f'{x} x {n} =', x * n )
    x = x + 1