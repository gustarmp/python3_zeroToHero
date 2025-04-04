# Exercicio 5.12
#Altere o programa anterior de forma a perguntar também o valor depositado mensalmente. Esse valor será depositado no início de cada mês, e você deve considerá-lo para o cálculo de juros do mês seguinte.

# PASSEI MAIS DE UMA HORA NESSE EXERCICIO, ESTA CERTO DA VISAO DO LIVRO, MAS NAO ME PARECE CERTO.
# VOU COLOCAR A RESPOSTA DO PROFESSOR COMENTADA ABAIXO DO MEU CODIGO. 
# AMBOS DAO VALORES DE JUROS IGUAIS MAS NAO DE GANHO NO ULTIMO MES. 
# ISSO SE DEVE AO PROFESSOR IMAGINAR QUE A PESSOA FARIA O DEPOSITO INICIAL + MENSAL NO PRIMEIRO MES.
# PEDI AO CHATGPT PARA CORRIGIR E ELE DISSE QUE OS DOIS ESTAO ERRADOS HAHAHA.

inicial = float(input('Qual o deposito inicial: R$ '))
mensal = float(input('Qual o valor depositado mensalmente: R$'))
juros = float(input('Qual a taxa de juros: ')) / 100
meses = 1
final = inicial

while meses <= 24:
    inicial = inicial + (inicial * juros)
    print(f'Valor do mes {meses}: R${inicial:.2f}')
    meses = meses + 1
    inicial = inicial + mensal
    
print(f'O ganho total com juros foi de: R${inicial - final:.2f}')

# depósito = float(input("Depósito inicial: "))
# taxa = float(input("Taxa de juros (Ex.: 3 para 3%): "))
# investimento = float(input("Depósito mensal: "))
# mês = 1
# saldo = depósito
# while mês <= 24:
#     saldo = saldo + (saldo * (taxa / 100)) + investimento
#     print(f"Saldo do mês {mês} é de R${saldo:5.2f}.")
#     mês = mês + 1
# print(f"O ganho obtido com os juros foi de R${saldo-depósito:8.2f}.")