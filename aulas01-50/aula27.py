"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""

variavel = 'Ola mundo'
print(variavel[:3]) # pegando do comeco ate o espaco
print(variavel[4:]) # pegando de "m" ate o fim da string
print(variavel[4:5]) # pegando apenas um caracter
print(variavel[0:9:1]) # o ultimo numero sao os passos, de quanto em quanto iremos "pular"
print(variavel[::-1]) # forma de inverter a string
print(len(variavel)) # conta a quantidade de caracteres de uma string
