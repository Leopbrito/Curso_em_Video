from random import randint
from time import sleep
from operator import itemgetter

def header(txt):
    print('-'*30)
    print(f'{txt:^30}')
    print('-'*30)

jogo = dict()
ranking = list()
header('Rodando os Dados')
for x in range(1,5):
    jogo[f'jogador{x}'] = randint(1,6)
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado')
    sleep(0.5)
header('Ranking')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{1}° lugar -> {v[0]} com {v[1]}')
    sleep(0.5)
