from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)

print('''========== JOKENPO ==========
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual sua jogada: '))
sleep(0.7)
print('JO')
sleep(0.7)
print('KEN')
sleep(0.7)
print('PO')
sleep(0.7)
print('''-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
O Computador jogou {}
Voce jogou {}
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-'''.format(itens[computador],itens[jogador]))
if computador == 0: # COMPUTADOR JOGOU PEDRA
    if jogador == 0:
        print('O JOGO EMPATOU!!!')
    elif jogador == 1:
        print('VOCE GANHOU!!!')
    elif jogador == 2:
        print('VOCE PERDEU!!!')
elif computador == 1: # COMPUTADOR JOGOU PAPEL
    if jogador == 0:
        print('VOCE PERDEU!!!')
    elif jogador == 1:
        print('O JOGO EMPATOU!!!')
    elif jogador == 2:
        print('VOCE GANHOU!!!')
elif computador == 2: # COMPUTADOR JOGOU PAPEL
    if jogador == 0:
        print('VOCE GANHOU!!!')
    elif jogador == 1:
        print('VOCE PERDEU!!!')
    elif jogador == 2:
        print('O JOGO EMPATOU!!!')