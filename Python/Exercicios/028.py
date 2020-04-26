from random import randint
from time import sleep

print('\033[1;34mVou pensar em um número entre 0 e 5. Tente advinhar...\033[0;0m')
numale = randint(0,5)
numesc = int(input('Em que número pensei: '))
while  numesc < 0 or numesc > 5:
    print('\033[31mVocê escolheu um número invalido!!!\033[m')
    numesc = int(input('Escolha um número entre 0 e 5: '))
print('\033[1;33mPROCESSANDO...\033[0;0m')
sleep(2)
if numale == numesc:
    print('\033[0;32mVocê acertou!!!, eu pensei no número {}.\033[0;0m'.format(numale))
else:
    print('\033[0;31mVocê Errou!!!, Eu pensei no número {} não no {}.\033[0;0m'.format(numale,numesc))