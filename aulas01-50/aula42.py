frase = 'O Python e uma linguagem de programacao multiparadigma. Python foi criado por Guido Van Rossum.'.lower()

i = 0
qtdApareceuMaisVezes = 0
letraApareceuMaisVezes = ''
while i < len(frase):
    letraAtual = frase[i]
    qtdLetra = frase.count(letraAtual)

    if qtdApareceuMaisVezes < qtdLetra:
        qtdApareceuMaisVezes = qtdLetra
        letraApareceuMaisVezes = letraAtual

    i += 1

print(f'A letra que apareceu mais vezes foi {letraApareceuMaisVezes} que apareceu {qtdApareceuMaisVezes}x.')