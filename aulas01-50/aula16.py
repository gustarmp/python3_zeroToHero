# if / elif      / else
# se / e se      / se nao

entrada = input('Voce quer "entrar" ou "sair?" ')

if entrada == 'entrar' or entrada == 'Entrar':
    print('Voce entrou no sistema.')
elif entrada == 'sair' or entrada == 'Sair':
    print('Voce saiu do sistema.')
else:
    print('Voce nao digitou uma opcao valida.')
