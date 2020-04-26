from random import randint
from time import sleep

print('\033[1;34mDigite um número entre 0 e 100, e eu vou tentar advinhar...\033[0;0m')
numesc = int(input('Em que número pensei: '))
numale = -1
cont = 0
soma = 0
while  numesc < 0 or numesc > 100:
    print('\033[31mVocê escolheu um número invalido!!!\033[m')
    numesc = int(input('Escolha um número entre 0 e 100: '))
while numesc != numale:
    cont = cont + 1
    numale = randint(0,100)
    soma = soma + numale
    print("{} - {}".format(cont,numale))
print('o sistema demorou {} tentativas para advinhar seu número'.format(cont))
print('A soma de todos os números tentados foi {}'.format(soma))