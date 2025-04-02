# Exercicio 4.11
# Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar. O valor da prestação mensal não pode ser superior a 30% do salário. Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.

valorCasa = float(input('Qual o valor do imovel?\n'))
salario = float(input('Qual o seu salario? \n'))
anos = int(input('Quantos anos voce pagara? \n'))
prestacaoMensal = valorCasa / (anos * 12) 
salarioPorcentagem = (prestacaoMensal / salario)* 100

if salarioPorcentagem > 30:
    print('Desculpe, nao podemos aprovar sua solicitacao de credito.')
else:
    print('Opa, vamos te dar dinheiro.')

print(f'A prestacao mensal de R${prestacaoMensal:.2f} equivale a {salarioPorcentagem:.2f}% do seu salario de R${salario:.2f}!')