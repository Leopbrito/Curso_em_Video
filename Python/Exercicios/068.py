from random import randint

print('-=-'*10)
print('  VAMOS JOGAR PAR OU IMPAR')
print('-=-'*10)
vitoria = 0
while True:
    computador = randint(0,10)
    jogador = int(input('Digite um valor: '))
    soma = computador + jogador
    parimpar = input('Par ou Impar? [P/I]: ').upper()
    print('---'*10)
    if soma % 2 == 0 and parimpar == 'P':
        vitoria += 1
        print(f'Voce jogou {jogador} e o computador jogou {computador}, A soma é {soma} DEU PAR')
        print('\033[32mVoce Venceu\033[m')
    elif soma % 2 == 1 and parimpar == 'I':
        vitoria += 1
        print(f'Voce jogou {jogador} e o computador jogou {computador}, A soma é {soma} DEU IMPAR')
        print('\033[32mVoce Venceu\033[m')
    elif soma % 2 == 0 and parimpar == 'I':
        print(f'Voce jogou {jogador} e o computador jogou {computador}, A soma é {soma} DEU PAR')
        print('\033[31mVoce Perdeu\033[m')
        break
    else:
        print(f'Voce jogou {jogador} e o computador jogou {computador}, A soma é {soma} DEU IMPAR')
        print('\033[31mVoce Perdeu\033[m')
        break
print('---'*10)
print(f'GAME OVER, Voce venceu {vitoria} vezes.')