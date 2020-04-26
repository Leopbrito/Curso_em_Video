frase = input('Digite uma frase: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('Voce digitou a frase {}'.format(junto))
print('A frase invertida fica {}'.format(inverso))
if junto == inverso:
    print('A frase É um palindromo')
else:
    print('A Frase NÃo É um palindromo')