# Exercicio 5.15
# Escreva um programa para controlar uma pequena máquina registradora. 
# Você deve solicitar ao usuário que digite o código do produto e a quantidade comprada. 
# Utilize a tabela de códigos a seguir para obter o preço de cada produto:

# Código Preço
# 1      0,50
# 2      1,00 
# 3      4,00
# 5      7,00
# 9      8,00

# Seu programa deve exibir o total das compras depois que o usuário digitar 0.
# Qualquer outro código deve gerar a mensagem de erro “Código inválido”.

soma = 0
codValido = 1, 2, 3, 5, 9

while True:
    codProputo = int(input('Digite o codigo do produto (0 para sair): '))
    if codProputo == 0:
        break
    if codProputo not in codValido:
        print('Codigo invalido.')
        continue
    qtdProduto = int(input('Digite a quantidade desse produto: '))
    if codProputo == 1:
        soma = soma + (qtdProduto * 0.50)
    elif codProputo == 2:
        soma = soma + (qtdProduto * 1.00)
    elif codProputo == 3:
        soma = soma + (qtdProduto * 4.00)
    elif codProputo == 5:
        soma = soma + (qtdProduto * 7.00)
    elif codProputo == 9:
        soma = soma + (qtdProduto * 8.00)

print(f'Total da compra: R${soma:.2f}')
