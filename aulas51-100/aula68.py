"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""

x = 1 # escopo do modulo, pode ser utilizado dentro de funcoes

def escopo():
    global x # dizendo que o x e uma variavel global, ou seja, o valor de x pode ser alterado dentro do escopo da funcao.
    x = 10 # escopo da funcao, variaveis so podem ser acessadas pela propria funcao.

    def outra_funcao():
        global x
        x = 11
        y = 2
        print(x, y)

    outra_funcao()
    print(x)


print(x)
escopo()
print(x)