# \r\n -> CRLF
# \n -> LF

print(12, 34, 1001, sep='-') #utilizando o sep= podemos escolher qual separador ficara entre os argumentos
print(56, 78, sep='.')
print(91, 12, sep=',')

# \r\n -> CRLF
# \n -> LF
print(12, 34, 1011, sep="", end='#')
print(56, 78, sep='-', end='\n')
print(9, 10, sep='-', end='\n')
