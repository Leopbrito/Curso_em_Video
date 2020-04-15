from random import sample
from time import sleep
jogos = list()
qtd = int(input('Quantos jogos voce quer que eu sorteie: '))
for x  in range(0, qtd):
    a = sample(range(1, 61), 6)
    print(f'Jogo {x+1}: {sorted(a)}')
    sleep(0.5)
