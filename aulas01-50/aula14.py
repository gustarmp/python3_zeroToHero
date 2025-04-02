a = 'AAAAAA'
b = 'B'
c = 1.1
string = 'a={0} a={0} a={0} b={1} c={2:.2f}' # Strings com valor vazio que serao informados na linha abaixo.
formato = string.format(a, b, c) # Preenchendo as strings com valor das variaveis.
# Os valores sao passados apenas quando utilizamos o .format, colocando os valores entre parenteses, seguindo a ordem que a string apresenta na variavel.

print(formato)