# Exercicio 5.8
# Escreva um programa que leia dois números. Imprima o resultado da multiplicação do primeiro pelo segundo. Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se de que podemos entender a multiplicação de dois números como somas sucessivas de um deles. Assim, 4 × 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.

# a = int(input('Digite o primeiro numero: '))
# b = int(input('Digite o segundo numero: '))
# resultado = 0
# contador = 0
# 
# while b < a:
#     a = a + resultado
#     print

# Codigo do exercicio resolvido, nao consegui concluir :(
p = int(input("Primeiro número: "))
s = int(input("Segundo número: "))
x = 1
r = 0
while x <= s:
    r = r + p
    x = x + 1
print(f"{p} x {s} = {r}")