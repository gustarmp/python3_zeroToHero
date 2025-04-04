"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""
# v1 = 'a'
# v2 = 'a'
# print(id(v1))
# print(id(v2))

condicao = False
passouNoIf = None


if condicao:
    passouNoIf = True
    print('Faca algo')
else:
    print('Nao faca algo')

print(passouNoIf, passouNoIf is None)
print(passouNoIf, passouNoIf is not None)

# Neste exemplo, a flag flag é usada como um indicador booleano, e a variável nome é inicializada com None para indicar que ainda não foi definida. 
# Isso ajuda a entender como esses conceitos podem ser aplicados em situações práticas.
nome = None
 
if nome is None:
    print("O nome ainda não foi definido.")
else:
    print("O nome é:", nome)