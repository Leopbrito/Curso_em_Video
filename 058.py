from random import randint
from time import sleep

tent = 1

print('\033[1;34mVou pensar em um número entre 0 e 10. Tente advinhar...\033[0;0m')
numale = randint(0,10)
numesc = int(input('Em que número pensei: '))
while  numesc < 0 or numesc > 10:
    print('\033[31mVocê escolheu um número invalido!!!\033[m')
    numesc = int(input('Escolha um número entre 0 e 10: '))
print('\033[1;33mPROCESSANDO...\033[0;0m')
sleep(2)
while numesc != numale:
    tent += 1
    if numesc > numale:
        print('Menos... Tente mais uma vez!')
        numesc = int(input('Qual seu novo palpite ? '))
    if numesc < numale:
        print('Mais... Tente mais uma vez!')
        numesc = int(input('Qual seu novo palpite ? '))
print(f'Voce acertou com {tent} tentativas.')