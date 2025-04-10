"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
# Esse codigo foi feito totalmente por mim.
# Estou a uma semana e meia aprendendo Python, sei que esta ruim
# em comparacao com o do professor, mas esta correto em 
# logica. Escrevendo para me lembrar daqui uns anos :)

cpf = str(input('Digite seu CPF: '))
noveDigito = cpf[:9]
listaCpf = []
listaCpfInt = []
multi = [10, 9, 8, 7, 6, 5, 4, 3, 2]
listaM = []
contador = 0
somador = 0

for c in cpf:
    listaCpf.append(c)

for i in listaCpf:
    numero = int(i)
    listaCpfInt.append(numero)

for i in range(9):
    multiLista = listaCpfInt[i] * multi[i]
    listaM.append(multiLista)

for s in listaM:
    somador += s

digito = (somador * 10) % 11
digitoNovo = digito if digito <= 9 else 0
# print(digitoNovo)

"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

# Essa parte do segundo digito fiz juntamente com o professor
# por conta disso esta bem melhor que a parte 1 hahaha
# Claro fiz algumas adaptacoes para funcionar com a parte 1. 

dezDigitos = noveDigito + str(digitoNovo)
contadorRegressivo = 11

resultadoDigito2 = 0
for d in dezDigitos:
    resultadoDigito2 += (int(d) * contadorRegressivo)
    contadorRegressivo -= 1
digito2 = ((resultadoDigito2 * 10) % 11) 
digitoNovo2 = digito2 if digito2 <=9 else 0

novoCpf = f'{noveDigito}{digitoNovo}{digitoNovo2}'

if cpf == novoCpf:
    print(f'{novoCpf} e valido!')

else:
    print(f'{novoCpf} invalido!')