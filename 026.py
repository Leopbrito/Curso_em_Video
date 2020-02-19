frase = input('Digite uma frase: ').strip()
print('A letra A apareceu {} vezes'.format(frase.lower().count('a')))
print('A primeira letra A apareceu na posição {}'.format(frase.lower().find('a')+1))
print('A ultima letra A apareceu na posição {}'.format(frase.lower().rfind('a')+1))