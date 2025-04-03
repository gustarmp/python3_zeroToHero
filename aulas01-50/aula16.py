# if / elif      / else
# se / e se      / se nao

entrada = input('Voce quer "entrar" ou "sair?" ').lower() # lower usado para formatar a string para tudo minusculo.

if entrada == 'entrar':
    print('Voce entrou no sistema.')
elif entrada == 'sair':
    print('Voce saiu do sistema.')
else:
    print('Voce nao digitou uma opcao valida.')
