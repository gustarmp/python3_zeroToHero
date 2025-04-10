"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""

numero1 = 0.14
numero2 = 0.724
soma = numero1 + numero2
print(f"{soma:.2f}")
print(round(soma)) # round usado para arredondar valores
print(round(soma, 3)) # segundo parametro para quantidade de casas decimais