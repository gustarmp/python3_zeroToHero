"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
palavra = 'Gelatina'.lower()
letraAcertadas = ''
tentativas = 0

while True:
    letra = input('Digite uma letra: ')
    tentativas += 1
    if len(letra) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra in palavra:
        letraAcertadas += letra
    
    palavraFormada = ''
    for letraSecreta in palavra:
        if letraSecreta in letraAcertadas:
            palavraFormada += letraSecreta
        else:
            palavraFormada += '*'
    print(palavraFormada)
    
    if palavraFormada == palavra:
        print(f'Voce acertou a palavra: {palavraFormada}')
        print(f'Tentativas necessarias: {tentativas}')
        break
    print(f'Tentativas: {tentativas}')