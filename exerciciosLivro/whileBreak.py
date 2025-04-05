# Exercicio 5.14
# Escreva um programa que leia números inteiros do teclado. O programa deve ler os números até que o usuário digite 0 (zero). No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética.

s = 0
c = 0

while True:
    v = int(input('Digite um valor para somar ou 0 para sair: '))
    if v == 0:
        break
    s += v # o mesmo que s = s + v
    c += 1 # o mesmo que c = c + 1
print(f'soma: {s} e numeros digitados: {c} e media: {s / c}')
