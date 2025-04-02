# nome = input('Qual o seu nome? ')
# print(f'O seu nome e {nome}.')

num1 = input('Digite um numero: ') # programa pode quebrar se fizer a coersao de tipo nessa variavel, sem a possibiliade de verificar o que o usuario digitou.
num2 = input('Digite outro numero: ')

intNum1 = int(num1) # fazendo essas variaveis de coersao evita que o programa quebre logo no comeco do codigo caso o usuario digite algo diferente de numeros.
intNum2 = int(num2)

print(f'A soma dos numeros e: {intNum1 + intNum2}')