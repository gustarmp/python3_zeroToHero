# Exercicio 4.4
# Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.

salario = float(input('Qual o seu salario: \n'))
base = salario
aumento10 = base * 0.10
aumento15 = base * 0.15

if base > 1250:
    novoSalario = base + aumento10
if base <= 1250:
    novoSalario = base + aumento15

print(f'Seu salario agora e de R${novoSalario:.2f}.')