# Capitulo 4.1.1
# Calculo de imposto de renda baseado no salario

salario = float(input('Digite o seu salario para calculo de imposto: \n'))
base = salario
imposto = 0

if base > 3000:
    imposto = imposto +((base - 3000) * 0.35)
    base = 3000
if base > 1000:
    imposto = imposto +((base - 1000) * 0.20)

print(f'Salario: R${salario:6.2f} Imposto a pagar: R${imposto:6.2f}')